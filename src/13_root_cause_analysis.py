# PURPOSE: Identify root causes affecting NPS

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
CHART_FOLDER = BASE_DIR / "outputs" / "charts"
REPORT_FOLDER = BASE_DIR / "outputs" / "reports"

TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(PROCESSED_FOLDER / "individual_featured.csv")

print("Dataset loaded successfully.")

print("\n" + "=" * 70)
print("ROOT CAUSE ANALYSIS")
print("=" * 70)

print(df.info())

print("\nFirst Five Records")
print(df.head())

# --------------------------------------------------
# IDENTIFY PROMOTERS, PASSIVES & DETRACTORS
# --------------------------------------------------

print("\n" + "=" * 70)
print("PROMOTERS, PASSIVES & DETRACTORS")
print("=" * 70)

# Summary
nps_summary = (
    df.groupby("NPS_Category")
      .agg(
          Participants=("Participant_ID", "count"),
          Average_NPS=("NPS", "mean")
      )
      .reset_index()
)

# Percentage
nps_summary["Percentage"] = (
    nps_summary["Participants"] /
    len(df) * 100
).round(2)

# Sort
category_order = ["Promoter", "Passive", "Detractor"]

nps_summary["NPS_Category"] = pd.Categorical(
    nps_summary["NPS_Category"],
    categories=category_order,
    ordered=True
)

nps_summary = nps_summary.sort_values("NPS_Category")

print(nps_summary)

# Save Table
nps_summary.to_csv(
    TABLE_FOLDER / "root_cause_nps_summary.csv",
    index=False
)

print("Root cause NPS summary table saved.")

# --------------------------------------------------
# Chart
# --------------------------------------------------

plt.figure(figsize=(6,5))

plt.bar(
    nps_summary["NPS_Category"],
    nps_summary["Participants"]
)

plt.title("Promoters, Passives & Detractors")

plt.xlabel("NPS Category")

plt.ylabel("Participants")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "root_cause_nps_summary.png",
    dpi=300
)

plt.close()

print("Root cause NPS summary chart saved.")

# --------------------------------------------------
# COMPARE ATTRIBUTE SCORES
# --------------------------------------------------

print("\n" + "=" * 70)
print("ATTRIBUTE SCORE COMPARISON")
print("=" * 70)

attributes = [
    "Job Relevance",
    "Content Clarity",
    "Learning Effectiveness",
    "Learner Engagement",
    "Trainer Facilitation",
    "Trainer Feedback Quality",
    "Learning Environment",
    "Overall Satisfaction"
]

attribute_summary = (
    df.groupby("NPS_Category")[attributes]
      .mean()
      .round(3)
      .T
      .reset_index()
      .rename(columns={"index": "Attribute"})
)

print(attribute_summary)

# Save Table
attribute_summary.to_csv(
    TABLE_FOLDER / "root_cause_attribute_comparison.csv",
    index=False
)

print("Root cause attribute comparison table saved.")

# --------------------------------------------------
# Chart
# --------------------------------------------------

plt.figure(figsize=(10,6))

for category in ["Promoter", "Passive", "Detractor"]:
    if category in attribute_summary.columns:
        plt.plot(
            attribute_summary["Attribute"],
            attribute_summary[category],
            marker="o",
            label=category
        )

plt.xticks(rotation=45, ha="right")

plt.ylabel("Average Rating")

plt.title("Attribute Scores by NPS Category")

plt.legend()

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "root_cause_attribute_comparison.png",
    dpi=300
)

plt.close()

print("Root cause attribute comparison chart saved.")


# --------------------------------------------------
# ROOT CAUSE GAP ANALYSIS
# --------------------------------------------------

print("\n" + "=" * 70)
print("ROOT CAUSE GAP ANALYSIS")
print("=" * 70)

# Get Promoter and Detractor averages
promoter_scores = (
    df[df["NPS_Category"] == "Promoter"][attributes]
    .mean()
)

detractor_scores = (
    df[df["NPS_Category"] == "Detractor"][attributes]
    .mean()
)

# Create Gap Analysis Table
gap_analysis = pd.DataFrame({
    "Attribute": attributes,
    "Promoter_Score": promoter_scores.values,
    "Detractor_Score": detractor_scores.values
})

gap_analysis["Gap"] = (
    gap_analysis["Promoter_Score"] -
    gap_analysis["Detractor_Score"]
).round(3)

gap_analysis = gap_analysis.sort_values(
    by="Gap",
    ascending=False
).reset_index(drop=True)

print(gap_analysis)

# Save Table
gap_analysis.to_csv(
    TABLE_FOLDER / "root_cause_gap_analysis.csv",
    index=False
)

print("Root cause gap analysis table saved.")

# --------------------------------------------------
# Gap Analysis Chart
# --------------------------------------------------

plt.figure(figsize=(10,6))

plt.bar(
    gap_analysis["Attribute"],
    gap_analysis["Gap"]
)

plt.xticks(rotation=45, ha="right")

plt.ylabel("Score Gap")

plt.title("Root Cause Gap Analysis")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "root_cause_gap_analysis.png",
    dpi=300
)

plt.close()

print("Root cause gap analysis chart saved.")

# --------------------------------------------------
# PRIORITY MATRIX
# --------------------------------------------------

print("\n" + "=" * 70)
print("PRIORITY MATRIX")
print("=" * 70)

# Calculate Overall Average Score
average_scores = df[attributes].mean()

priority_matrix = gap_analysis.copy()

priority_matrix["Average_Score"] = (
    average_scores[
        priority_matrix["Attribute"]
    ].values
)

# Higher gap + lower average = higher priority
priority_matrix["Priority_Score"] = (
    priority_matrix["Gap"] *
    (4 - priority_matrix["Average_Score"])
).round(3)

priority_matrix = priority_matrix.sort_values(
    by="Priority_Score",
    ascending=False
).reset_index(drop=True)

print(priority_matrix)

# Save Table
priority_matrix.to_csv(
    TABLE_FOLDER / "root_cause_priority_matrix.csv",
    index=False
)

print("Root cause priority matrix table saved.")

# --------------------------------------------------
# Priority Matrix Chart
# --------------------------------------------------

plt.figure(figsize=(10,6))

plt.bar(
    priority_matrix["Attribute"],
    priority_matrix["Priority_Score"]
)

plt.xticks(rotation=45, ha="right")

plt.ylabel("Priority Score")

plt.title("Root Cause Improvement Priority")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "root_cause_priority_matrix.png",
    dpi=300
)

plt.close()

print("Root cause priority matrix chart saved.")

# --------------------------------------------------
# ROOT CAUSE ANALYSIS REPORT
# --------------------------------------------------

print("\n" + "=" * 70)
print("ROOT CAUSE ANALYSIS REPORT")
print("=" * 70)

report_file = REPORT_FOLDER / "root_cause_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 70 + "\n")
    file.write("ROOT CAUSE ANALYSIS REPORT\n")
    file.write("=" * 70 + "\n\n")

    file.write("Dataset Summary\n")
    file.write("-" * 35 + "\n")
    file.write(f"Total Participants : {len(df)}\n\n")

    file.write("NPS Category Summary\n")
    file.write("-" * 35 + "\n")
    file.write(nps_summary.to_string(index=False))
    file.write("\n\n")

    file.write("Attribute Comparison\n")
    file.write("-" * 35 + "\n")
    file.write(attribute_summary.to_string(index=False))
    file.write("\n\n")

    file.write("Root Cause Gap Analysis\n")
    file.write("-" * 35 + "\n")
    file.write(gap_analysis.to_string(index=False))
    file.write("\n\n")

    file.write("Priority Matrix\n")
    file.write("-" * 35 + "\n")
    file.write(priority_matrix.to_string(index=False))
    file.write("\n\n")

    file.write("Top 5 Improvement Priorities\n")
    file.write("-" * 35 + "\n")

    top5 = priority_matrix.head(5)

    for _, row in top5.iterrows():
        file.write(
            f"{row['Attribute']} "
            f"(Priority Score = {row['Priority_Score']:.3f})\n"
        )

print("Root cause analysis report generated successfully.")
print(f"Report saved at : {report_file}")