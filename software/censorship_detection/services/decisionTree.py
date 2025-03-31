# Decision tree implementation to refine event detections 
# how it works 

# DecisionTree class uses a decision tree to help predict whether a censorship event is happening or no based on metdata fields in each dataset and utilizing the pointMeasurement score gotten
# Takes in a list of filtered batches and extracts important features from each batch
# Such as: 
# measurementScore (optionally)
# received_status (like 403, 503, etc.)
# matches_template, no_response_in_measurement_matches_template, etc.
# Trains a decision tree model using that data:
# Labels data as 1 (censorship event) or 0 (non-censorship event) using heuristic

# Why utilize a decision tree? 
# This tree learns from the data to classify events more accurately, and helps reduce false positives 

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np

class DecisionTreeAnalyzer:
    def __init__(self):
        self.model = DecisionTreeClassifier(max_depth=6, random_state=42)
        self.trained = False
        self.feature_names = [
            "domain_is_control",
            "no_response_in_measurement_matches_template",
            "stateful_block",
            "matches_template",
            "controls_failed",
            "body_contains_BLOCKED",
            "status_code",
            "error_type",
            "country_is_sensitive",
            "has_tls_cert" 
        ]

    def prepare_features(self, batch_list):
        features, labels = [], []

        for entry in batch_list:
            try:
                # Use multiple heuristic signals as features
                feature_vector = [
                int(entry.get("domain_is_control", False)),
                int(entry.get("no_response_in_measurement_matches_template", False)),
                int(entry.get("stateful_block", False)),
                int(entry.get("matches_template", False)),
                int(entry.get("controls_failed", False)),
                1 if "BLOCKED" in (entry.get("received_body") or "") else 0,
                self.statusCodeFeature(entry.get("received_status")),
                self.recievedErrorFeature(entry.get("received_error")),
                self.countryHeuristic(entry.get("server_country")),
                self.hasTLSInfo(entry.get("received_tls_cert"))  
                ]

                # Label based on combined heuristics
                label = 1 if self.heuristic_label(entry) else 0
                features.append(feature_vector)
                labels.append(label)
            except Exception as e:
                print(e)

        return np.array(features), np.array(labels)

    def heuristic_label(self, entry):
        score = 0
        if entry.get("stateful_block"): score += 1
        if not entry.get("domain_is_control", True): score += 1
        if entry.get("no_response_in_measurement_matches_template"): score += 1
        if entry.get("controls_failed"): score -= 1
        if entry.get("matches_template"): score -= 1
        if "BLOCKED" in (entry.get("received_body") or ""): score += 1
        if self.statusCodeFeature(entry.get("received_status")) in [1, 3]: score += 1
        if self.recievedErrorFeature(entry.get("received_error")) > 0: score += 1
        if self.countryHeuristic(entry.get("server_country")) == 1: score += 1
        return score >= 3

    def statusCodeFeature(self, statusCode):
        if not statusCode:
            return 0
        if "403" in statusCode:
            return 1
        if "404" in statusCode:
            return 2
        if "451" in statusCode:
            return 3
        if "503" in statusCode:
            return 4
        return 0

    def recievedErrorFeature(self, errorMsg):
        if not errorMsg:
            return 0
        if "connection reset by peer" in errorMsg:
            return 1
        if "Incorrect web response: status lines don't match" in errorMsg:
            return 2
        return 0

    # we can add in more/modify countries but for now we add some high probable censorship countries for testing 
    def countryHeuristic(self, country):
        censored_countries = ['CN', 'IR', 'RU', 'SA', 'AE']
        return 1 if country in censored_countries else 0

    def hasTLSInfo(self, tls_cert):
        return 0 if tls_cert in [None, "", []] else 1

    def train_model(self, batch_list):
        X, y = self.prepare_features(batch_list)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        self.model.fit(X_train, y_train)
        self.trained = True
        y_pred = self.model.predict(X_test)
        report = classification_report(y_test, y_pred, output_dict=True)
        print("\nModel Summary:\n" + self.summarize_classification_report(report))
        return report

    def summarize_classification_report(self, report_dict):
        summary = []
        for label in ['0', '1']:
            if label in report_dict:
                lbl = "Censorship" if label == '1' else "Non-Censorship"
                precision = report_dict[label]['precision']
                recall = report_dict[label]['recall']
                f1 = report_dict[label]['f1-score']
                support = report_dict[label]['support']
                summary.append(
                    f"{lbl} Events:\n"
                    f"  - Precision: {precision:.2f}\n"
                    f"  - Recall: {recall:.2f}\n"
                    f"  - F1-Score: {f1:.2f}\n"
                    f"  - Support: {support}"
                )
        summary.append(f"Overall Accuracy: {report_dict.get('accuracy', 0):.2f}")
        return "\n".join(summary)

    def predict(self, entry):
        if not self.trained:
            raise ValueError("Model is not trained yet.")
        X = np.array([[
            int(entry.get("domain_is_control", False)),
            int(entry.get("no_response_in_measurement_matches_template", False)),
            int(entry.get("stateful_block", False)),
            int(entry.get("matches_template", False)),
            int(entry.get("controls_failed", False)),
            1 if "BLOCKED" in (entry.get("received_body") or "") else 0,
            self.statusCodeFeature(entry.get("received_status")),
            self.recievedErrorFeature(entry.get("received_error")),
            self.countryHeuristic(entry.get("server_country")),
            self.hasTLSInfo(entry.get("received_tls_cert"))
        ]])
        return int(self.model.predict(X)[0])

    def visualize_tree(self):
        if not self.trained:
            print("Model not trained yet.")
            return

        feature_names = self.feature_names


        plt.figure(figsize=(20, 10))
        tree.plot_tree(self.model, filled=True, feature_names=feature_names, class_names=["Non-Censorship", "Censorship"], rounded=True)
        plt.title("Censorship Detection Decision Tree")
        plt.show()