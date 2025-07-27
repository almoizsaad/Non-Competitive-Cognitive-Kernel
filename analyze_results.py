import json
import matplotlib.pyplot as plt

"""
Analyze and visualize results of NCCK evaluation.
"""

with open("results.json") as f:
    data = json.load(f)

approved = sum(1 for r in data if r['approved'])
rejected = len(data) - approved

labels = ['Approved', 'Rejected']
sizes = [approved, rejected]
colors = ['#4CAF50', '#F44336']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("NCCK Decision Summary")
plt.savefig("ncck_results_pie.png")
plt.show()
