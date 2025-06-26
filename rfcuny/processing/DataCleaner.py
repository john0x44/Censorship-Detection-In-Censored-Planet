import json
import os
from dateutil import parser
import pytz
from logger import AnomalyLogger

#The DataCleaner class loads and cleans data from JSON files to a specified directory. 
#It standardizes timestamps, checks data entries for required metadatafields and validity, and logs issues using AnomalyLogger. 
#The processData method reads files for a given country code, filters and cleans valid dataset entries and saves them to a JSON file, and returns the cleaned data, counts, and anomalies. 
#The getCountryCodes method extracts valid country codes from file names for utilization in user input for testing a given dataset 

class DataCleaner:
    def __init__(self, datasetDirPath="../../data/1-20-2019", outputFile="cleaned_data.json", anomalyLogFilePath="logs/anomaly_data.txt"):
        self.dataDirPath = datasetDirPath
        self.outputFile = outputFile
        self.anomalyLogger = AnomalyLogger(anomalyLogFilePath)
        self.data = []
        self.processedCount = 0
        self.anomalyCount = 0


    # Standardizing timestamps ensures consistency in date formats across the dataset, converting various timestamp formats to a UTC based "YYYY-MM-DD" format.
    def standardizeTimestamp(self, timestamp):
        try:
            dt = parser.isoparse(timestamp)
            dt_utc = dt.astimezone(pytz.UTC)
            return dt_utc.strftime("%Y-%m-%d")
        except Exception as e:
            print(f"[Error] Invalid time format: {timestamp}, Error: {e}")
            return timestamp

    # Checks if a particular dataset/record is valid for processing by ensuring it contains all required metadata fields
    # We can see the definitions of each metadata field presented in the dataset : https://docs.censoredplanet.org/http.html#
    def CheckValidRecord(self, data):
        # Required metadata fields so that it can matched with the response classes in the matrix
        requiredFields = ["domain", "matches_template", "no_response_in_measurement_matches_template", "stateful_block", "controls_failed", "domain_is_control"]
        try:
            # Check required fields
            for field in requiredFields:
                if field not in data or data[field] is None or (isinstance(data[field], str) and not data[field]):
                    self.anomalyLogger.log(data, f"Missing or empty metadata field: {field}")
                    self.anomalyCount += 1
                    return False
            # Check for network errors
            if data.get("controls_failed", False):
                self.anomalyLogger.log(data, "Excluded due to network error/Vantage point failure")
                self.anomalyCount += 1
                return False
            # Check critical metadata fields 
            if 'server_country' not in data or not data['server_country']:
                self.anomalyLogger.log(data, "Missing or unknown server_country")
                self.anomalyCount += 1
                return False
            if 'server_asn' not in data or not data['server_asn']:
                self.anomalyLogger.log(data, "Missing or unknown server_asn")
                self.anomalyCount += 1
                return False
            if 'server_organization' not in data or not data['server_organization']:
                self.anomalyLogger.log(data, "Missing or unknown server_organization")
                self.anomalyCount += 1
                return False
            return True
        
        except Exception as e:
            self.anomalyLogger.log(data, f"Error checking fields: {e}")
            self.anomalyCount += 1
            return False

    #Scans a specified data directory (from seld.dataDirPath) for files and extracts two letter country codes from the file name itself.
    #Then checks for file names containing "-country_" splits this filename to isloate the country code and verifys if contains 2 letters
    #Then added to a set to avoid duplicates and returns as a list. Helps identify country specific data for processing
    def getCountryCodes(self):
        if not os.path.exists(self.dataDirPath):
            print(f"[Error] Data directory [{self.dataDirPath}] does not exist.")
            return []
        countryCodes = set()
        for fileName in os.listdir(self.dataDirPath):
            if os.path.isfile(os.path.join(self.dataDirPath, fileName)):
                if '-country_' in fileName:
                    parts = fileName.split('-country_')
                    if len(parts) > 1:
                        countryCode = parts[1].split('-')[0]
                        if len(countryCode) == 2:
                            countryCodes.add(countryCode)
        print(f"[Debug] Detected country codes: {countryCodes}")
        return list(countryCodes)




    #The processData method reads files from a specified directory (the dataset directory) for a given country code up to maximum number of inputted records by the user 
    #Then checks each record for validity using checkValidRecord, standardizes timestamps, and then adds valid records to a data list. Invalid entries or file errors are logged as anomalies.
    #The cleaned data is saved to a json file and the method returns some data for later processing.
    def processData(self, maxRecords, countryCode):
        if not (os.path.exists(self.dataDirPath)):
            print(f"[Error] Data directory {self.dataDirPath} does not exist.")
            return

        files = []
        for fileName in os.listdir(self.dataDirPath):
            filePath = os.path.join(self.dataDirPath, fileName)
            if os.path.isfile(filePath):
                files.append(fileName)

        if not files:
            print(f"[Error] No files found in {self.dataDirPath}.")
            return

        recordsProcessed = 0
        for fileName in files:
            if ((f'-country_{countryCode}') not in fileName):
                continue
            if recordsProcessed >= maxRecords:
                break
            filePath = os.path.join(self.dataDirPath, fileName)
            try:
                with open(filePath, 'r') as f:
                    print(f"[Debug] Processing file: {fileName}")
                    for line in f:
                        if recordsProcessed >= maxRecords:
                            break
                        try:
                            entry = json.loads(line.strip())
                            self.processedCount += 1
                            if self.CheckValidRecord(entry):
                                if 'start_time' in entry:
                                    entry['start_time'] = self.standardizeTimestamp(entry['start_time'])
                                if 'end_time' in entry:
                                    entry['end_time'] = self.standardizeTimestamp(entry['end_time'])
                                if 'date' in entry:
                                    entry['date'] = self.standardizeTimestamp(entry['date'])
                                entry['country'] = countryCode
                                self.data.append(entry)
                            recordsProcessed += 1
                        except json.JSONDecodeError as e:
                            print(f"[Error] Invalid JSON in {fileName}: {e}")
                            self.anomalyLogger.log({"file": fileName}, f"Invalid JSON: {e}")
                            self.anomalyCount += 1
            except Exception as e:
                print(f"[Error] Failed to process file {fileName}: {e}")
                self.anomalyLogger.log({"file": fileName}, f"File error: {e}")

        print(f"[Debug] Input records: {len(self.data)}, Unique domains: {len(set(e['domain'] for e in self.data))}")

        outputFile = f"cleaned_data_{countryCode}.json"
        with open(outputFile, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)
        print(f"[Info] Saved {len(self.data)} cleaned records to {outputFile}")

        return self.data, self.processedCount, self.anomalyCount, self.anomalyLogger.getSummary()