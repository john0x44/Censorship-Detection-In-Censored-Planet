import requests
from collections import defaultdict
from PySide2.QtWidgets import QLabel, QVBoxLayout
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from functools import partial 

#ScoreReportManager : Class used to check if our own measurement score censored event list matches confirmed censored events, and shows us a summary report 

class ScoreReportManager:
    def __init__(self, reportUI, showUIButton):
        self.showUIButton = showUIButton 

        self.reportUI = reportUI
        self.countryConfirmedDomains = defaultdict(set)  
        self.userDetectedDomains = defaultdict(set)     
        self.showUIButton.clicked.connect(partial(self.showScoreReportUI))

    def showScoreReportUI(self):
        self.reportUI.MainWindow.show() 

    #Request to OONI measurement tool kit 
    def getConfirmedOONI(self, country_code):
        url = f"https://api.ooni.org/api/v1/aggregation?probe_cc={country_code}&test_name=web_connectivity&since=2019-01-20&until=2019-01-21&axis_x=measurement_start_day&axis_y=domain&time_grain=day"
        try:
            data = requests.get(url).json()
            confirmed = set()
            for entry in data.get("result", []):
                if entry.get("confirmed_count", 0) == 1:
                    confirmed.add(entry.get("domain", "").strip().lower())
            self.countryConfirmedDomains[country_code] = confirmed
        except Exception as e:
            print(f"[ScoreReport] Failed to fetch OONI data for {country_code}: {e}")

    def collectUserDetectedDomains(self, censoredEvents):
        self.userDetectedDomains.clear()
        for entry in censoredEvents:
            domain = entry.get("domain", "").strip().lower()
            country = entry.get("server_country", "").strip().upper()
            if domain and country:
                self.userDetectedDomains[country].add(domain)

    def calculateAccuracy(self):
        total_detected = 0
        total_correct = 0
        matched_domains = []  

        for country, detected_domains in self.userDetectedDomains.items():
            if country not in self.countryConfirmedDomains:
                self.getConfirmedOONI(country)

            confirmed = self.countryConfirmedDomains[country]
            matches = detected_domains.intersection(confirmed) #intersection of both sets 
            total_detected += len(detected_domains)
            total_correct += len(matches)

            for domain in matches:
                matched_domains.append((country, domain)) 

        accuracy = (total_correct / total_detected) * 100 if total_detected else 0
        return total_detected, total_correct, accuracy, matched_domains

    def updateUI(self):
        detected, correct, accuracy, matched_domains = self.calculateAccuracy()

        
        print("[ScoreReportManager][LOG] [Matched Domains]")
        for country, domain in matched_domains:
            print(f"{domain} [Country: {country}]")

        allDomains = "<b style='color:white;'>Detected Censored Domains:</b><br><br>"
        matchedDomains= set((c, d) for c, d in matched_domains)

        for country, domains in self.userDetectedDomains.items():
            for domain in sorted(domains):
                if (country, domain) in matchedDomains:
                    allDomains += f"<span style='color:#45ff89;'>[MATCHED] {domain} ({country})</span><br>"
                #else:
                    #allDomains += f"<span style='color:white;'>[NOT-MATCHED] {domain} ({country})</span><br>"

        self.reportUI.label_3.setStyleSheet("color:white; font-size: 13px;")
        self.reportUI.label_3.setText(allDomains)

        self.reportUI.label_2.setStyleSheet("color: white; font-size: 14px;")
        self.reportUI.label_2.setText(f"""
            <b>Score Report</b><br>
            Total Detected Events: <span style='color:#ffaa00;'>{detected}</span><br>
            Correctly Matched with OONI: <span style='color:#00ff88;'>{correct}</span><br>
            Accuracy Score: <span style='color:#45ff89;'>{accuracy:.2f}%</span>
        """)

        
        layout = self.reportUI.frame_4.layout()
        if layout is None:
            layout = QVBoxLayout()
            self.reportUI.frame_4.setLayout(layout)
        else:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        #Implement QPieSeries : 
        # https://doc.qt.io/qt-6/qpieseries.html
        #  
        series = QtCharts.QPieSeries()
        if correct > 0:
            series.append("Correct", correct)
            series.slices()[-1].setBrush(QColor("#45ff89"))
        if detected - correct > 0:
            series.append("Incorrect", detected - correct)
            series.slices()[-1].setBrush(QColor("#ff4c4c"))

        series.setHoleSize(0.3)
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Detection Accuracy")
        chart.setTitleBrush(QColor("white"))
        chart.setBackgroundBrush(QColor("#121212"))
        chart.legend().setLabelColor(QColor("white"))
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QtCharts.QChartView(chart)
        chart_view.setStyleSheet("background: transparent;")

        layout.addWidget(chart_view)
