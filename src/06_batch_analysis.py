# PURPOSE : Batch Level Analysis

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
TABLE_FOLDER.mkdir(parents=True, exist_ok=True)

CHART_FOLDER = BASE_DIR / "outputs" / "charts"
CHART_FOLDER.mkdir(parents=True, exist_ok=True)

REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# ==========================================================
# LOAD BATCH DATASET
# ==========================================================

batch_df = pd.read_csv(
    PROCESSED_FOLDER / "batch_featured.csv"
)

print("Batch dataset loaded successfully.")

print("\n" + "=" * 70)
print("BATCH DATASET INFORMATION")
print("=" * 70)

print(batch_df.info())

print("\nFirst Five Records")
print(batch_df.head())

# ==========================================================
# BATCH SUMMARY
# ==========================================================

batch_summary = (
    batch_df
    .groupby("Batch No")
    .agg(
        Participants=("Participant_ID", "count"),
        Average_NPS=("NPS", "mean"),
        Promoters=("Is_Promoter", "sum"),
        Passives=("Is_Passive", "sum"),
        Average_Content_Index=("Content_Quality_Index", "mean"),
        Average_Trainer_Index=("Trainer_Effectiveness_Index", "mean"),
        Average_Environment_Index=("Learning_Environment_Index", "mean")
    )
    .reset_index()
)

batch_summary["Promoter_Percentage"] = (
    batch_summary["Promoters"]
    / batch_summary["Participants"]
) * 100

batch_summary = batch_summary.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("BATCH SUMMARY")
print("=" * 70)

print(batch_summary)

batch_summary.to_csv(
    TABLE_FOLDER / "batch_analysis.csv",
    index=False
)

print("Batch analysis table saved.")

# ==========================================================
# BATCH ANALYSIS CHART
# ==========================================================

plt.figure(figsize=(12,6))

plt.bar(
    batch_summary["Batch No"],
    batch_summary["Average_NPS"]
)

plt.title("Average NPS by Batch")

plt.xlabel("Batch")

plt.ylabel("Average NPS")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "batch_analysis.png"
)

plt.close()

print("Batch chart saved.")

# ==========================================================
# BEST & WORST PERFORMING BATCHES
# ==========================================================

print("\n" + "=" * 70)
print("BEST & WORST PERFORMING BATCHES")
print("=" * 70)

print("\nTop 5 Batches")
print(
    batch_summary[
        ["Batch No", "Average_NPS", "Promoter_Percentage"]
    ].head(5)
)

print("\nBottom 5 Batches")
print(
    batch_summary[
        ["Batch No", "Average_NPS", "Promoter_Percentage"]
    ].tail(5)
)

# ==========================================================
# BATCH ANALYSIS REPORT
# ==========================================================

report_file = REPORT_FOLDER / "batch_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 70 + "\n")
    file.write("BATCH ANALYSIS REPORT\n")
    file.write("=" * 70 + "\n\n")

    file.write(f"Total Batches : {batch_summary.shape[0]}\n")
    file.write(f"Total Participants : {batch_summary['Participants'].sum()}\n\n")

    file.write("TOP 5 BATCHES\n")
    file.write("-" * 50 + "\n")
    file.write(
        batch_summary[
            ["Batch No", "Average_NPS", "Promoter_Percentage"]
        ]
        .head(5)
        .to_string(index=False)
    )

    file.write("\n\n")

    file.write("BOTTOM 5 BATCHES\n")
    file.write("-" * 50 + "\n")
    file.write(
        batch_summary[
            ["Batch No", "Average_NPS", "Promoter_Percentage"]
        ]
        .tail(5)
        .to_string(index=False)
    )

print("\nBatch analysis report generated successfully.")
print(f"Report saved at : {report_file}")