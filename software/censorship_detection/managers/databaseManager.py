from collections import Counter
from datetime import datetime
import sqlite3
from PySide2.QtWidgets import QLabel
from functools import partial


#SQL Documentation : https://docs.python.org/3/library/sqlite3.html
#SQL Video : https://www.youtube.com/watch?v=pd-0G0MigUA
#SQL Video : https://www.youtube.com/watch?v=girsuXz0yA8

class DatabaseManager:
    def __init__(self, databaseUI, databaseButton, filterTimeUI, domainSearchUI, countrySearchUI):
        self.domainSearchUI = domainSearchUI
        self.countrySearchUI = countrySearchUI
        self.databaseButton = databaseButton
        self.databaseUI = databaseUI
        self.filterTimeUI = filterTimeUI

        self.conn = sqlite3.connect("datasets.db")
        self.cursor = self.conn.cursor()
        self.createTables()


        
        self.totalAnomaliesLabel = self.databaseUI.label_8
        self.topCountryLabel = self.databaseUI.label_9
        self.totalCensorshipLabel = self.databaseUI.label_10
        self.topDomainsLabel = self.databaseUI.label_12
        self.showFilterTimeButton = self.databaseUI.pushButton_7

        #CountrySearch UI button 
        self.showCountrySearchButton = self.databaseUI.pushButton_9
        self.showCountrySearchButton.clicked.connect(partial(self.showCountrySearchUI))
        #domainSearch UI button 
        self.showDomainSearchUIButton = self.databaseUI.pushButton_8
        self.showDomainSearchUIButton.clicked.connect(partial(self.showDomainSearchUI))

        #CountrySearch 
        self.countrySearchButton = self.countrySearchUI.pushButton_2
        self.countrySearchButton.clicked.connect(partial(self.searchCountry))

        #DomainSearch 
        self.domainSearchButton = self.domainSearchUI.pushButton_2
        self.domainSearchButton.clicked.connect(partial(self.searchDomain))

        #Filter time UI button 
        self.filterTimeButton = self.filterTimeUI.pushButton_2
        self.filterTimeButton.clicked.connect(partial(self.filterTime))

        # Highlight Feature 
        self.high_censor_countries = {"CN", "RU", "AE"}

        
        self.databaseButton.clicked.connect(partial(self.showDatabaseList))
        self.showFilterTimeButton.clicked.connect(partial(self.showFilterTimeUI))


    def extractTopCensorshipReasons(self, entries):
        reasonsCounter = Counter()

        for entry in entries:
            body = (entry.get("received_body") or "").lower()
            error = (entry.get("received_error") or "").lower()

            if "connection reset by peer" in error:
                reasonsCounter["connection reset by peer"] += 1
            if "status lines don't match" in error:
                reasonsCounter["HTTP status mismatch"] += 1
            if "blocked" in body:
                reasonsCounter["BLOCKED in body"] += 1

        return reasonsCounter.most_common(3)  

    # Run when searching for a country onto the searchcountry UI 
    def searchCountry(self):
        countryInput = self.countrySearchUI.lineEdit.text().strip().upper()
        if not countryInput:
            print("[SearchCountry][LOG] Empty.")
            return

        self.conn.commit() 
        
        self.cursor.execute(
            """
            SELECT start_time, domain, server_country, score
            FROM censored_events
            WHERE UPPER(server_country) = ?
            """,
            (countryInput,)
        )

        results = self.cursor.fetchall()
        entries = []
        for row in results:
            entry = {
                "start_time": row[0],
                "domain": row[1],
                "server_country": row[2],
                "score": row[3]
            }
            entries.append(entry)

        self.loadCensoredEvents(entries)

    # Run when searching for a domain onto the searchdomain UI 
    def searchDomain(self):
        domainInput = self.domainSearchUI.lineEdit.text().strip().lower()
        if not domainInput:
            print("[SearchDomain][LOG] Empty.")
            return

        self.conn.commit()

        print(f"[SearchDomain][DEBUG] Client searching for: {domainInput}")

        try:
            self.cursor.execute(
                """
                SELECT start_time, domain, server_country, score
                FROM censored_events
                WHERE LOWER(TRIM(domain)) LIKE ?
                """,
                (f"%{domainInput}%",)
            )

            results = self.cursor.fetchall()
            entries = []
            for row in results:
                entries.append({
                    "start_time": row[0],
                    "domain": row[1],
                    "server_country": row[2],
                    "score": row[3]
                })

            self.loadCensoredEvents(entries)

        except Exception as error:
            print(f"[SearchDomain][ERROR] Query failed: {error}")


    def showCountrySearchUI(self):
        self.countrySearchUI.MainWindow.show() 
    
    def showDomainSearchUI(self):
        self.domainSearchUI.MainWindow.show() 

    #Format input time string from user 
    def parseMilitaryTime(self, timeStr):
        try:
            dt = datetime.strptime(timeStr, "%H:%M")
            return dt.strftime("%H:%M:%S")
        except ValueError:
            return None
    
    def filterTime(self):
        input = self.filterTimeUI.lineEdit.text().strip()
        if not input or "-" not in input:
            print("[FilterTime][LOG] Invalid format. Use ie, - 01:25-14:24")
            return

        try:
            start_raw, end_raw = input.split("-")
            start_time = self.parseMilitaryTime(start_raw.strip())
            end_time = self.parseMilitaryTime(end_raw.strip())

            if not start_time or not end_time:
                print("[FilterTime] Invalid time format.")
                return

            self.cursor.execute(
                """
                SELECT start_time, domain, server_country, score
                FROM censored_events
                WHERE TIME(start_time) >= TIME(?) AND TIME(start_time) <= TIME(?)
                """,
                (start_time, end_time)
            )

            results = self.cursor.fetchall()
            entries = []
            for row in results:
                entry = {
                    "start_time": row[0],
                    "domain": row[1],
                    "server_country": row[2],
                    "score": row[3]
                }
                entries.append(entry)

            self.loadCensoredEvents(entries)

        except Exception as error:
            print(f"[FilterTime][LOG] Error: {error}")
        
    def showFilterTimeUI(self):
        self.filterTimeUI.MainWindow.show() 

    def createTables(self):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS anomalies (
                timestamp TEXT, domain TEXT, server_country TEXT, reason TEXT,
                UNIQUE(timestamp, domain)
            )
            ''')
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS censored_events (
                start_time TEXT, domain TEXT, server_country TEXT, score REAL,
                UNIQUE(start_time, domain)
            )
            ''')
        self.conn.commit()

    def showDatabaseList(self):
        print("[DatabaseUI LOG] Showing UI")
        self.databaseUI.MainWindow.show()

    def clearArea(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def loadAnomalies(self, anomalies):
        layout = self.databaseUI.scrollAreaWidgetContents.layout()
        self.clearArea(layout)

        for entry in anomalies:
            self.cursor.execute(
                "INSERT OR IGNORE INTO anomalies (timestamp, domain, server_country, reason) VALUES (?, ?, ?, ?)",
                (entry["timestamp"], entry["domain"], entry["server_country"], entry["reason"])
            )
            label = QLabel(f"{entry['timestamp']} - DOMAIN: {entry['domain']} | COUNTRY: {entry['server_country']} | REASON: {entry['reason']}")
            label.setStyleSheet("color: lightgray;")
            layout.addWidget(label)

        self.conn.commit()
        self.updateAnomalyStats()

    def loadCountries(self, summary):
        layout = self.databaseUI.scrollAreaWidgetContents_2.layout()
        self.clearArea(layout)

        for country, count in summary.items():
            label = QLabel(f"{country}: {count} censorship events")
            label.setStyleSheet("color: lightgray;")
            layout.addWidget(label)

    def loadCensoredEvents(self, entries):
        topReasons = self.extractTopCensorshipReasons(entries)
        print(topReasons)
        layout = self.databaseUI.scrollAreaWidgetContents_3.layout()
        self.clearArea(layout)

        for entry in entries:
            try:
                self.cursor.execute(
                    """
                    INSERT OR IGNORE INTO censored_events (start_time, domain, server_country, score)
                    VALUES (?, ?, ?, ?)
                    """,
                    (entry["start_time"], entry["domain"], entry["server_country"], entry["score"])
                )

                color = "yellow" if entry["server_country"] in self.high_censor_countries else "lightgray"
                label = QLabel(f"{entry['start_time']} - DOMAIN: {entry['domain']} | COUNTRY: {entry['server_country']} | SCORE: {entry['score']:.2f}")
                label.setStyleSheet(f"color: {color};")
                layout.addWidget(label)

            except Exception as error:
                print(f"[loadCensoredEvents][ERROR] Failed to insert - {error}")

        self.conn.commit()

        self.updateCensorshipStats()

    def updateAnomalyStats(self):
        self.cursor.execute("SELECT COUNT(*) FROM anomalies")
        count = self.cursor.fetchone()[0]
        self.totalAnomaliesLabel.setText(f"Total Anomalies: {count}")

    def updateCensorshipStats(self):
        self.cursor.execute("SELECT COUNT(*) FROM censored_events")
        total = self.cursor.fetchone()[0]
        self.totalCensorshipLabel.setText(f"Total Censorship Events: {total}")

        self.cursor.execute(
        """
            SELECT server_country, COUNT(*) as cnt 
            FROM censored_events 
            GROUP BY server_country 
            ORDER BY cnt DESC 
            LIMIT 1
        """
        )
        result = self.cursor.fetchone()
        if result:
            self.topCountryLabel.setText(f"Top Country: {result[0]} ({result[1]} Events)")
        else:
            self.topCountryLabel.setText("Top Country: N/A")

        self.cursor.execute(
        """
            SELECT domain, COUNT(*) as cnt 
            FROM censored_events 
            GROUP BY domain 
            ORDER BY cnt DESC 
            LIMIT 3
        """
        )
        topDomains = [row[0] for row in self.cursor.fetchall()]
        if topDomains:
            self.topDomainsLabel.setText("Top Domains Censored: " + ", ".join(topDomains))
        else:
            self.topDomainsLabel.setText("Top Domains Censored: [NONE]")