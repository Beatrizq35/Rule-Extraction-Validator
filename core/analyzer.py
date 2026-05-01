import pandas as pd
import os

class MetricAnalyzer:
    @staticmethod
    def load_ground_truth(csv_path):
        """Carrega as regras do CSV de gabarito."""
        if not os.path.exists(csv_path):
            return None
        df = pd.read_csv(csv_path)
        return df['rule'].tolist()

    @staticmethod
    def calculate_recall(expected_rules, extracted_text):
        """Calcula a revocação e identifica o que foi perdido."""
        found = []
        missing = []
        
        text_lower = extracted_text.lower()
        
        for rule in expected_rules:
            if rule.strip().lower() in text_lower:
                found.append(rule)
            else:
                missing.append(rule)
        
        total = len(expected_rules)
        recall = (len(found) / total) if total > 0 else 0
        
        return recall, found, missing