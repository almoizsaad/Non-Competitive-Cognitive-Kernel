import json
from ncck_engine import NCCK

"""
Run simulations using NCCK model and generate result reports.
"""

ncck = NCCK()

with open("test_cases.json") as f:
    cases = json.load(f)

results = []
for case in cases:
    result = ncck.assess(case)
    case_result = {"id": case["id"], **result}
    results.append(case_result)

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
