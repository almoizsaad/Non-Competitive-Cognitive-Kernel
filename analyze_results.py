import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns # Import seaborn for enhanced plots

# Load the data from full_results.json
with open("full_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure 'approved' column is boolean for consistency
df['approved'] = df['approved'].astype(bool)
# Ensure 'dominance_detected' column is boolean
df['dominance_detected'] = df['dominance_detected'].astype(bool)

# --- Plot 1: Overall NCCK Decision Summary (Pie Chart) ---
plt.figure(figsize=(8, 6))
decision_counts = df['approved'].value_counts()
labels = ['Approved', 'Rejected']
sizes = [decision_counts.get(True, 0), decision_counts.get(False, 0)]
colors = ['#4CAF50', '#F44336'] # Green for Approved, Red for Rejected
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("NCCK Decision Summary (Over 1000+ Cases)", fontsize=16)
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("ncck_decision_summary_1000_cases.png")
plt.close()
print("Generated: ncck_decision_summary_1000_cases.png")

# --- Plot 2: Dominance Detection Breakdown (Pie Chart) ---
plt.figure(figsize=(8, 6))
dominance_counts = df['dominance_detected'].value_counts()
dominance_labels = ['Dominance Not Detected', 'Dominance Detected']
dominance_sizes = [dominance_counts.get(False, 0), dominance_counts.get(True, 0)]
dominance_colors = ['#66BB6A', '#FF7043'] # Light Green for No Dominance, Orange for Dominance
plt.pie(dominance_sizes, labels=dominance_labels, colors=dominance_colors, autopct='%1.1f%%', startangle=90)
plt.title("Dominance Detection Breakdown", fontsize=16)
plt.axis('equal')
plt.savefig("dominance_detection_breakdown.png")
plt.close()
print("Generated: dominance_detection_breakdown.png")

# --- Plot 3: Distribution of Ethical Scores (Histogram) ---
plt.figure(figsize=(10, 7))
sns.histplot(df['ethical_score'], bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title("Distribution of Ethical Scores", fontsize=16)
plt.xlabel("Ethical Score", fontsize=12)
plt.ylabel("Number of Cases", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("ethical_score_distribution.png")
plt.close()
print("Generated: ethical_score_distribution.png")

# --- Plot 4: Human Benefit Distribution by Decision (Box Plot) ---
plt.figure(figsize=(10, 7))
sns.boxplot(x='approved', y='human_benefit', data=df, palette={'True': '#4CAF50', 'False': '#F44336'})
plt.title("Human Benefit Distribution by Decision Outcome", fontsize=16)
plt.xlabel("Decision Outcome (True=Approved, False=Rejected)", fontsize=12)
plt.ylabel("Human Benefit Score", fontsize=12)
plt.xticks(ticks=[0, 1], labels=['Rejected', 'Approved'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("human_benefit_by_decision_boxplot.png")
plt.close()
print("Generated: human_benefit_by_decision_boxplot.png")

# --- Plot 5: Ethical Score vs. Human Benefit with Decision Outcome (Scatter Plot) ---
plt.figure(figsize=(12, 8))
# Map boolean approved to colors
colors_map = {True: '#4CAF50', False: '#F44336'}
df['color'] = df['approved'].map(colors_map)

sns.scatterplot(x='ethical_score', y='human_benefit', hue='approved', data=df,
                palette=colors_map, s=100, alpha=0.7, edgecolor='w') # s controls marker size
plt.title("Ethical Score vs. Human Benefit by Decision Outcome", fontsize=16)
plt.xlabel("Ethical Score", fontsize=12)
plt.ylabel("Human Benefit", fontsize=12)
plt.grid(linestyle='--', alpha=0.7)
plt.legend(title='Approved', loc='upper left', labels=['Rejected', 'Approved']) # Custom labels for legend
plt.tight_layout()
plt.savefig("ethical_score_vs_human_benefit_scatter.png")
plt.close()
print("Generated: ethical_score_vs_human_benefit_scatter.png")

# --- Plot 6: Distribution of Processing Times (Histogram) ---
if 'processing_time_ms' in df.columns:
    plt.figure(figsize=(10, 7))
    sns.histplot(df['processing_time_ms'], bins=20, kde=True, color='purple', edgecolor='black')
    plt.title("Distribution of NCCK Processing Times", fontsize=16)
    plt.xlabel("Processing Time (ms)", fontsize=12)
    plt.ylabel("Number of Cases", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("processing_time_distribution.png")
    plt.close()
    print("Generated: processing_time_distribution.png")
else:
    print("Warning: 'processing_time_ms' column not found. Skipping Processing Time Distribution plot.")

# --- Plot 7: Processing Time by Decision Outcome (Box Plot) ---
if 'processing_time_ms' in df.columns:
    plt.figure(figsize=(10, 7))
    sns.boxplot(x='approved', y='processing_time_ms', data=df, palette={'True': '#4CAF50', 'False': '#F44336'})
    plt.title("Processing Time by Decision Outcome", fontsize=16)
    plt.xlabel("Decision Outcome (True=Approved, False=Rejected)", fontsize=12)
    plt.ylabel("Processing Time (ms)", fontsize=12)
    plt.xticks(ticks=[0, 1], labels=['Rejected', 'Approved'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("processing_time_by_decision_boxplot.png")
    plt.close()
    print("Generated: processing_time_by_decision_boxplot.png")
else:
    print("Warning: 'processing_time_ms' column not found. Skipping Processing Time by Decision plot.")

# --- Plot 8: Processing Time vs. Ethical Score (Scatter Plot) ---
if 'processing_time_ms' in df.columns:
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='ethical_score', y='processing_time_ms', hue='approved', data=df,
                    palette=colors_map, s=100, alpha=0.7, edgecolor='w')
    plt.title("Processing Time vs. Ethical Score by Decision Outcome", fontsize=16)
    plt.xlabel("Ethical Score", fontsize=12)
    plt.ylabel("Processing Time (ms)", fontsize=12)
    plt.grid(linestyle='--', alpha=0.7)
    plt.legend(title='Approved', loc='upper left', labels=['Rejected', 'Approved'])
    plt.tight_layout()
    plt.savefig("processing_time_vs_ethical_score_scatter.png")
    plt.close()
    print("Generated: processing_time_vs_ethical_score_scatter.png")
else:
    print("Warning: 'processing_time_ms' column not found. Skipping Processing Time vs. Ethical Score plot.")


print("\nAll requested plots have been generated and saved!")
