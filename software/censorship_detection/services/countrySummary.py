#summarizes how many censorship events were detected per country

from collections import defaultdict

class CountrySummary:
    def __init__(self):
        self.summary = defaultdict(int)

    def getSummary(self):
        return dict(self.summary)  

    def update(self, entry):
        country = entry.get("server_country", "Unknown")
        if entry.get("score", 0) > 0.5:  # We can modify this later 
            self.summary[country] += 1

    def printSummary(self):
        print("[Censorship Events by Country]")
        for country, count in sorted(self.summary.items(), key=lambda x: x[1], reverse=True):
            print(f"{country}: {count}")

