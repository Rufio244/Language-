class TivterSystem:
    def __init__(self):
        self.age_groups = ["0–6","7–12","13–18","19–60","60+"]
        self.methods = {
            "0–6": ["Sound association","Visual match"],
            "7–12": ["Pattern build","Story immersion"],
            "13+": ["Root logic","Context mapping"]
        }
    def get_method(self, age: str):
        return self.methods.get(age, ["Standard"])

