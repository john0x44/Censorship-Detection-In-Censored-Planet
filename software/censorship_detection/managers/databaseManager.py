from PySide2.QtWidgets import QLabel
from functools import partial

class DatabaseManager:

    def __init__(self, databaseUI, databaseButton):
        self.databaseButton = databaseButton 
        self.databaseUI = databaseUI

        self.databaseUI.pushButton_2.clicked.connect(partial(self.saveAnomaliesDB))
        self.databaseUI.pushButton_3.clicked.connect(partial(self.saveCountriesDB))
        self.databaseUI.pushButton_4.clicked.connect(partial(self.saveCensoredDB))
        self.databaseButton.clicked.connect(partial(self.showDatabaseList))

    def showDatabaseList(self):
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
            label = QLabel(f"{entry['timestamp']} - DOMAIN: {entry['domain']} | COUNTRY: {entry['server_country']} | REASON: {entry['reason']}")
            label.setStyleSheet("color: lightgray;")
            layout.addWidget(label)

    def loadCountries(self, summary):
        layout = self.databaseUI.scrollAreaWidgetContents_2.layout()
        self.clearArea(layout)

        for country, count in summary.items():
            label = QLabel(f"{country}: {count} censorship events")
            label.setStyleSheet("color: lightgray;")
            layout.addWidget(label)

    def loadCensoredEvents(self, entries):
        layout = self.databaseUI.scrollAreaWidgetContents_3.layout()
        self.clearArea(layout)

        for entry in entries:
            label = QLabel(f"{entry['start_time']} - DOMAIN: {entry['domain']} | COUNTRY: {entry['server_country']} | SCORE: {entry['score']:.2f}")
            label.setStyleSheet("color: lightgray;")
            layout.addWidget(label)


    def saveAnomaliesDB(self):
        print("Saving anomalies to database...")

    def saveCountriesDB(self):
        print("Saving country summary to database...")

    def saveCensoredDB(self):
        print("Saving censored events to database...")
