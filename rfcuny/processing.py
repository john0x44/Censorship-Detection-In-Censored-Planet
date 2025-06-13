import json
import os
from datetime import datetime
import pytz
from dateutil import parser

#Utilizing the same methods from the software project from 4900 into one simpler and moduler based code 

class AnomalyLogger:
    def __init__(self, log_file="logs/anomalies_log.txt"):
        self.log_file = log_file
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        self.recent_anomalies = [] #Cache recent anomalies 

    def log(self, entry, reason):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        #We can insert more missing metadata fields later on but these are the important ones such as makin sure domain is present
        anomaly_entry = {
            "timestamp": timestamp,
            "domain": entry.get("domain", "Unknown"),
            "server_country": entry.get("server_country", "Unknown"),
            "reason": reason
        }
        self.recent_anomalies.append(anomaly_entry)
        #save anomaly log for later analysis
        with open(self.log_file, "a") as f:
            f.write(json.dumps(anomaly_entry) + "\n")

    def get_summary(self):
        return self.recent_anomalies

class DataCleaner:
    def __init__(self, data_dir="./data/1-20-2019", output_file="cleaned_data.json", anomaly_log_file="logs/anomalies_log.txt"):
        self.data_dir = data_dir
        self.output_file = output_file
        self.anomaly_logger = AnomalyLogger(anomaly_log_file)
        self.cleaned_data = []
        self.processed_count = 0
        self.anomaly_count = 0

    def standardize_timestamp(self, timestamp):
        try:
            dt = parser.isoparse(timestamp)
            dt_utc = dt.astimezone(pytz.UTC)
            return dt_utc.strftime("%Y-%m-%d %H:%M:%S.%f")
        except Exception as e:
            print(f"[Error] Invalid time format: {timestamp}, Error: {e}")
            return timestamp

    def can_use_entry(self, entry):
        required_fields = [
            "domain",
            "no_response_in_measurement_matches_template",
            "stateful_block",
            "controls_failed",
            "domain_is_control"
        ]
        try:
            for field in required_fields:
                if field not in entry or entry[field] is None or (type(entry[field])==str and entry[field] == ''):
                    self.anomaly_logger.log(entry, f"Metadata field is empty or not present, Metadata field : [{field}]")
                    self.anomaly_count += 1
                    return False
            return True
        except Exception as e:
            self.anomaly_logger.log(entry, f"Error checking fields: {e}")
            self.anomaly_count += 1
            return False

    # Extract country codes from each filename in parse like fashion
    def get_country_codes(self):
        if not os.path.exists(self.data_dir):
            return []
        country_codes = set()
        for file_name in os.listdir(self.data_dir):
            if file_name.endswith('') and '-country_' in file_name:
                # If dataset filename is something different than the one present in directory
                try:
                    parts = file_name.split('-country_')
                    if len(parts) > 1:
                        country_code = parts[1].split('.')[0] 
                        country_codes.add(country_code)
                except Exception:
                    continue
        return list(country_codes)

    def process_data(self, max_records, country_code):
        if not os.path.exists(self.data_dir):
            print(f"[Error] Data directory {self.data_dir} does not exist.")
            return

        # Search and filter files by country code
        files = [f for f in os.listdir(self.data_dir) if f.endswith('') and f'-country_{country_code}' in f]
        if not files:
            print(f"[Error] No files found for country {country_code} in {self.data_dir}.")
            return

        records_processed = 0
        for file_name in files:
            if records_processed >= max_records:
                break
            file_path = os.path.join(self.data_dir, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if records_processed >= max_records:
                            break
                        try:
                            entry = json.loads(line.strip())
                            self.processed_count += 1
                            if self.can_use_entry(entry):
                                # Fixing timestamps
                                if 'start_time' in entry:
                                    entry['start_time'] = self.standardize_timestamp(entry['start_time'])
                                if 'end_time' in entry:
                                    entry['end_time'] = self.standardize_timestamp(entry['end_time'])
                                entry['country_code'] = country_code
                                self.cleaned_data.append(entry)
                            records_processed += 1
                        except json.JSONDecodeError as e:
                            print(f"[Error] Invalid {file_name} {e}")
                            self.anomaly_logger.log({"File": file_name}, f"Invalid line: {e}")
                            self.anomaly_count += 1
            except Exception as e:
                print(f"[Error] Failed to process file {file_name}: {e}")
                self.anomaly_logger.log({"file": file_name}, f"File processing error: {e}")

        # Save cleaned data to file
        output_file = f"cleaned_data_{country_code}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.cleaned_data, f, indent=4)
        print(f"[Info] Saved {len(self.cleaned_data)} cleaned records to {output_file}")

        print("\n[Data Processing Summary]")
        print(f"Total records processed: {self.processed_count}")
        print(f"Anomalies detected: {self.anomaly_count}")
        print(f"Total valid records: {len(self.cleaned_data)}")
        print("\n[Detected Anomalies]")
        for anomaly in self.anomaly_logger.get_summary()[-5:]:
            print(f"Domain: {anomaly['domain']} | Country: {anomaly['server_country']} | Time: {anomaly['timestamp']} | Reason: {anomaly['reason']}")

def main():
    try:
        max_records = int(input("Enter the number of records to process: "))
        if max_records <= 0:
            print("[Error] Please enter greater than 0")
            return
    except ValueError:
        print("[Error] Invalid input please enter number.")
        return

    cleaner = DataCleaner()
    country_codes = cleaner.get_country_codes()
    if not country_codes:
        print("[Error] No valid country codes found in the data directory.")
        return

    print("\nAvailable country codes:", ", ".join(country_codes))
    country_code = input("Enter country code: ").strip().upper()
    if country_code not in country_codes:
        print(f"[Invalidation Error] Please choose from: {', '.join(country_codes)}")
        return

    cleaner.process_data(max_records, country_code)

if __name__ == "__main__":
    main()