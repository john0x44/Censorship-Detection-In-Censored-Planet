# log the censorship events into a file 
import datetime

class CensorshipLogger:
    def __init__(self, log_file_path="censorship_log.txt"):
        self.log_file_path = log_file_path

    def log(self, entry):
        timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        domain = entry.get("domain", "Unknown")
        country = entry.get("server_country", "Unknown")
        score = entry.get("score", 0)
        reason = f"High Score ({score:.2f})"

        log_line = f"[{timestamp}] DOMAIN: {domain}, COUNTRY: {country}, SCORE: {score:.2f} | REASON: {reason}\n"
        
        with open(self.log_file_path, "a", encoding="utf-8") as f:
            f.write(log_line)
