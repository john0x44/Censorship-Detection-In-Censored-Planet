#Log anomalies within the datset such as missing/malformed metadata so dataset can be error free in the future for analysis
#The AnomalyLogger class logs issues or anomalies found in data processing. It saves details like the timestamp, domain, country, and reason for each anomaly to a file in the directory (logs/anomaly_log.txt) and keeps a list of recent anomalies in memory. 
#The log method records an anomaly with the given data and reason, while getSummary returns the list of all recorded anomalies.

import json
import os
from datetime import datetime
import pytz

class AnomalyLogger:
    def __init__(self, logFilePath="logs/anomaly_log.txt"):
        self.logFile = logFilePath
        os.makedirs(os.path.dirname(self.logFile), exist_ok=True)
        self.recentAnomalies = []

    def log(self, data, reason):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        #Handle incomplete data using get instead of direct access on the array data["domain"] as it would crash the software
        anomalyEntry = {
            "timestamp": timestamp,
            "domain": data.get("domain", "Unknown"),
            "country": data.get("country", "Unknown"),
            "reason": reason
        }
        self.recentAnomalies.append(anomalyEntry)
        with open(self.logFilePath, "a") as f:
            f.write(json.dumps(anomalyEntry) + "\n")
    
    def getSummary(self):
        return self.recentAnomalies
    
