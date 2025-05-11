# Connect dashboard UI to backend 
# Add some necessary configurations 

from functools import partial 

class DashboardManager:

    def __init__(self, mainUI, dashboardUI):
        self.mainUI = mainUI 
        self.dashboardUI = dashboardUI
        self.dashboardButton = self.mainUI.pushButton_7
    
        self.dashboardButton.clicked.connect(partial(self.openDashboard))
        self.topBlockedTextBox = self.dashboardUI.label_3

    def openDashboard(self):
        self.dashboardUI.MainWindow.show()
    
    def updateTopBlockedDomains(self, batchesProcessed):
        domain_counts = {}

        for batch in batchesProcessed:
            if 'batch' not in batch:
                continue
            for sub_batch in batch['batch'].values():
                for entry in sub_batch:
                    if entry.get('prediction') == 1:  
                        domain = entry.get('domain', 'UNKNOWN')
                        domain_counts[domain] = domain_counts.get(domain, 0) + 1

        sortedDomains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)
        topDomains = sortedDomains[:5]

        if not topDomains:
            display = "No censored domains found."
        else:
            display = "Top Blocked Domains:\n"
            for domain, count in topDomains:
                display += f"{domain}: {count} times\n"

        self.topBlockedTextBox.setText(display)

    def updateDashboard(self, dataProcessedInfo):
        self.openDashboard()
        eventRate = (dataProcessedInfo['detected']/dataProcessedInfo['processed'])*100
        self.dashboardUI.label_5.setText(f"EVENT RATE: %{eventRate}")
        #self.dashboardUI.label_3.setText(f"EVENTS PROCESSED: {dataProcessedInfo['processed']}")
        self.dashboardUI.label_4.setText(f"ANOMALIES DETECTED: {dataProcessedInfo['anomalies']}/{dataProcessedInfo['processed']}")
        self.dashboardUI.label_2.setText(f"EVENTS DETECTED: {dataProcessedInfo['detected']}/{dataProcessedInfo['processed']}")