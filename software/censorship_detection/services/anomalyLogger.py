import os
import json
from datetime import datetime

# Class gets the anomalies into a log file
class AnomalyLogger:
    def __init__(self, log_file="logs/anomalies_log.txt"):
        self.log_file = log_file
        self.recent_anomalies = []

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def getAnomalies(self):
        return self.recent_anomalies

    def log(self, batch):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "domain": batch.get("domain", "Unknown"),
            "server_country": batch.get("server_country", "Unknown"),
            "reason": "Missing critical fields"
        }

        self.recent_anomalies.append(entry)
        if len(self.recent_anomalies) > 5:
            self.recent_anomalies.pop(0)

        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def get_summary(self):
        return self.recent_anomalies
