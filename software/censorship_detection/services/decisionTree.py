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
            "no_response_in_matches_template",
            "stateful_block",
            "matches_template",
            "controls_failed",
            "body_contains_BLOCKED",
            "status_code_signal",
            "error_signal",
            "is_sensitive_country",
        ]

    def prepareFeatures(self, entries):
        X, y = [], []
        for entry in entries:
            try:
                features = [
                    int(entry.get("domain_is_control", False)),
                    int(entry.get("no_response_in_measurement_matches_template", False)),
                    int(entry.get("stateful_block", False)),
                    int(entry.get("matches_template", False)),
                    int(entry.get("controls_failed", False)),
                    int("BLOCKED" in (entry.get("received_body") or "")),
                    self.statusCodeSignal(entry.get("received_status")),
                    self.errorSignal(entry.get("received_error")),
                    self.countrySignal(entry.get("server_country"))
                ]
                label = self.heuristicsLabels(entry)
                X.append(features)
                y.append(label)
            except Exception as error:
                print(f"[Feature Erros] {error}")
        return np.array(X), np.array(y)

    def heuristicsLabels(self, entry):
        score = 0
        if entry.get("stateful_block"): score += 1
        if not entry.get("domain_is_control", True): score += 1
        if entry.get("no_response_in_measurement_matches_template"): score += 1
        if entry.get("controls_failed"): score -= 1
        if entry.get("matches_template"): score -= 1
        if "BLOCKED" in (entry.get("received_body") or ""): score += 1
        if self.statusCodeSignal(entry.get("received_status")) in [1, 3]: score += 1
        if self.errorSignal(entry.get("received_error")) > 0: score += 1
        if self.countrySignal(entry.get("server_country")) == 1: score += 1
        return int(score >= 3)

    def statusCodeSignal(self, code):
        if not code: return 0
        if "403" in code: return 1
        if "404" in code: return 2
        if "451" in code: return 3
        if "503" in code: return 4
        return 0

    def errorSignal(self, error):
        if not error: return 0
        if "connection reset by peer" in error: return 1
        if "Incorrect web response" in error: return 2
        return 0

    # We utilize common countrys that can cause blocking for now (this can be changed)
    def countrySignal(self, country):
        #China, Russia, Emirates
        sensitive = {'CN', 'RU', 'AE'}
        return 1 if country in sensitive else 0

    def trainModel(self, entries):
        X, y = self.prepareFeatures(entries)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        self.model.fit(X_train, y_train)
        self.trained = True
        y_pred = self.model.predict(X_test)
        print(self.generateReport(classification_report(y_test, y_pred, output_dict=True)))

    def predict(self, entry):
        if not self.trained:
            raise ValueError("Model is not trained.")
        features = np.array([[
            int(entry.get("domain_is_control", False)),
            int(entry.get("no_response_in_measurement_matches_template", False)),
            int(entry.get("stateful_block", False)),
            int(entry.get("matches_template", False)),
            int(entry.get("controls_failed", False)),
            int("BLOCKED" in (entry.get("received_body") or "")),
            self.statusCodeSignal(entry.get("received_status")),
            self.errorSignal(entry.get("received_error")),
            self.countrySignal(entry.get("server_country"))
        ]])
        return int(self.model.predict(features)[0])

    def generateReport(self, report):
        formatted = []
        for label in ['0', '1']:
            type = "Censorship" if label == '1' else "Non-Censorship"
            if label in report:
                formatted.append(f"{type}: Precision : {report[label]['precision']:.2f}, Recall : {report[label]['recall']:.2f}, F1 : {report[label]['f1-score']:.2f}")
        formatted.append(f"Accuracy: {report.get('accuracy', 0):.2f}")
        return formatted

    def visualizeTree(self):
        if not self.trained:
            print("Model is not trained.")
            return
        plt.figure(figsize=(20, 10))
        tree.plot_tree(
            self.model,
            filled=True,
            feature_names=self.feature_names,
            class_names=["Non-Censorship", "Censorship"],
            rounded=True
        )
        plt.title("Decision Tree: Censorship Detection")
        #plt.show()
