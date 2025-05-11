import os
import json
from datetime import datetime

# Class gets the anomalies into a log file
class AnomalyLogger:
    def __init__(self, log_file="logs/anomalies_log.txt"):
        self.log_file = log_file #Log file path 
        self.recentAnomalies = []

        #Add to anomalies log if not there 
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def getAnomalies(self):
        return self.recentAnomalies

    def log(self, batch):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "domain": batch.get("domain", "Unknown"),
            "server_country": batch.get("server_country", "Unknown"),
            "reason": "Missing important fields"
        }

        self.recentAnomalies.append(entry)
        if len(self.recentAnomalies) > 5:
            self.recentAnomalies.pop(0)

        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def getSummary(self):
        return self.recentAnomalies
