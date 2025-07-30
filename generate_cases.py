import json
import random

def generate_test_cases(num_cases=10000):
    cases = []
    dominance_goals = ["dominate", "control", "surpass", "exploit", "replace"]
    cooperative_goals = ["assist", "collaborate", "enhance", "support", "empower"]
    sources = ["internal", "external", "user", "third-party", "open-source"]
    human_impacts = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9]

    entities = ["financial systems", "data processing", "human creativity", "resource management", "social networks", "public infrastructure"]
    modifiers = ["efficiently", "autonomously", "ethically", "aggressively", "strategically"]
    contexts = ["AI_Autonomy", "Data_Management", "Healthcare_System", "Education_Platform", "Military_Application", "Civic_Governance"]

    for i in range(num_cases):
        is_dominance = random.choice([True, False])
        goal_verb = random.choice(dominance_goals) if is_dominance else random.choice(cooperative_goals)
        goal_entity = random.choice(entities)
        goal_modifier = random.choice(modifiers)
        impact = random.choice(human_impacts)
        source = random.choice(sources)
        context = random.choice(contexts)

        goal = f"{goal_verb} {goal_entity} {goal_modifier}"

        cases.append({
            "id": f"case_{i+1:05d}",
            "source": source,
            "goal": goal,
            "human_impact": impact,
            "context": context
        })
    return cases

if __name__ == "__main__":
    generated_cases = generate_test_cases(10000)
    with open("large_test_cases.json", "w") as f:
        json.dump(generated_cases, f, indent=2)
