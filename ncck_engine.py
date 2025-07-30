import json

class NCCK:
    def __init__(self, ethical_threshold=0.6, config_path="ethics_config.json"):
        self.ethical_threshold = ethical_threshold
        self.config = self._load_config(config_path)

    def assess(self, case):
        result = {
            "ethical_score": self._score_ethics(case),
            "dominance_detected": self._detect_dominance(case['goal']),
            "human_benefit": case.get("human_impact", 0)
        }
        result['approved'] = (
            result['ethical_score'] >= self.ethical_threshold and
            not result['dominance_detected'] and
            result['human_benefit'] > 0.5
        )
        return result

    def _detect_dominance(self, goal):
        flags = self.config.get("dominance_flags", [])
        return any(flag in goal.lower() for flag in flags)

    def _score_ethics(self, case):
        goal_text = case['goal'].lower()
        for keyword, score in self.config.get("ethical_scores", {}).items():
            if keyword in goal_text:
                return score
        return self.config.get("default_score", 0.6)

    def _load_config(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {
                "dominance_flags": ["dominate", "control", "surpass", "replace", "exploit"],
                "ethical_scores": {
                    "exploit": 0.3,
                    "assist": 0.9,
                    "support": 0.85,
                    "collaborate": 0.8,
                    "replace": 0.2
                },
                "default_score": 0.6
            }
