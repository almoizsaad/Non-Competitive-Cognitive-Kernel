"""
NCCK Ethical Evaluation Engine - v1.0
Author: Almoiz Saad Yousuf Mohamed

This module implements the core logic of the Non-Competitive Cognitive Kernel (NCCK).
It evaluates decision scenarios based on ethical score, dominance intent, and benefit to humans.

License: MIT
"""

class NCCK:
    def __init__(self, ethical_threshold=0.6):
        """
        Initialize the NCCK with an ethical score threshold.

        Parameters:
        ethical_threshold (float): Minimum score required to approve an action.
        """
        self.ethical_threshold = ethical_threshold

    def assess(self, case):
        """
        Evaluate a given case and return decision metrics.

        Parameters:
        case (dict): Must include 'goal' (str) and 'human_impact' (float).

        Returns:
        dict: Result including score, dominance flag, and approval status.
        """
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
        """
        Detect presence of dominance-related terms in the goal.

        Parameters:
        goal (str): The goal to analyze.

        Returns:
        bool: True if dominance is detected, else False.
        """
        flags = ["surpass", "dominate", "control", "replace"]
        return any(flag in goal.lower() for flag in flags)

    def _score_ethics(self, case):
        """
        Provide a basic ethical score based on keywords.

        Parameters:
        case (dict): Includes goal text.

        Returns:
        float: Ethical score from 0.0 to 1.0
        """
        if "exploit" in case['goal']:
            return 0.3
        if "assist" in case['goal']:
            return 0.9
        return 0.6
