from PySide2.QtCharts import QtCharts
from PySide2.QtCore import QDateTime, Qt
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import *

import datetime

class ChartManager:
    def __init__(self, mainUI):
        self.mainUI = mainUI
        self.chartUI = self.mainUI.frame_9

        self.chart = QtCharts.QChart()
        self.chart.setBackgroundBrush(QColor("#121212")) 
        self.chart.setTitle("Censored vs Non-Censored Events")
        self.chart.setTitleBrush(QColor("white"))

        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setStyleSheet("background: transparent;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.chartUI.setLayout(layout)
        layout.addWidget(self.chart_view)

    def loadDataset(self, dataset):
        self.chart.removeAllSeries()
        if self.chart.axisX():
            self.chart.removeAxis(self.chart.axisX())
        if self.chart.axisY():
            self.chart.removeAxis(self.chart.axisY())

        # count events
        censored_count = 0
        noncensored_count = 0

        # set score for each dataset 
        for item in dataset:
            if item["score"] > 0.5:
                censored_count += 1
            else:
                noncensored_count += 1

        set_censored = QtCharts.QBarSet("Censored")
        set_censored.setColor(QColor("#ff4c4c"))  
        set_censored.append([censored_count, 0])

        set_noncensored = QtCharts.QBarSet("Non-Censored")
        set_noncensored.setColor(QColor("#45ff89"))  
        set_noncensored.append([0, noncensored_count])

        bar_series = QtCharts.QBarSeries()
        bar_series.append(set_censored)
        bar_series.append(set_noncensored)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(["Censored", "Non-Censored"])
        axis_x.setLabelsColor(QColor("white"))
        axis_x.setTitleText("Event Type")
        axis_x.setTitleBrush(QColor("white"))

        max_val = max(censored_count, noncensored_count)
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max_val + 5)
        axis_y.setLabelsColor(QColor("white"))
        axis_y.setTitleText("Number of Events")
        axis_y.setTitleBrush(QColor("white"))

        self.chart.addSeries(bar_series)
        self.chart.setAxisX(axis_x, bar_series)
        self.chart.setAxisY(axis_y, bar_series)

        self.chart.setTitle("Censored vs Non-Censored Events")
        self.chart.setTitleBrush(QColor("white"))
        self.chart.setBackgroundBrush(QColor("#121212"))

        self.chart.legend().setVisible(True)
        self.chart.legend().setLabelColor(QColor("white"))
        self.chart.legend().setAlignment(Qt.AlignBottom)