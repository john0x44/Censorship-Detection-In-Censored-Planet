# Connect dashboard UI to backend 
# Add some necessary configurations 

from functools import partial 

class DashboardManager:

    def __init__(self, mainUI, dashboardUI):
        self.mainUI = mainUI 
        self.dashboardUI = dashboardUI
        self.dashboardButton = self.mainUI.pushButton_7

        self.dashboardButton.clicked.connect(partial(self.openDashboard))
    
    def openDashboard(self):
        self.dashboardUI.MainWindow.show()
    
    def updateDashboard(self, dataProcessedInfo):
        self.openDashboard()
        eventRate = (dataProcessedInfo['detected']/dataProcessedInfo['processed'])*100
        self.dashboardUI.label_5.setText(f"SUCCESS RATE: %{eventRate}")
        self.dashboardUI.label_3.setText(f"EVENTS PROCESSED: {dataProcessedInfo['processed']}")
        self.dashboardUI.label_4.setText(f"ANOMALIES DETECTED: {dataProcessedInfo['anomalies']}/{dataProcessedInfo['processed']}")
        self.dashboardUI.label_4.setText(f"EVENTS DETECTED: {dataProcessedInfo['detected']}/{dataProcessedInfo['processed']}")