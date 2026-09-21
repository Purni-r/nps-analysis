# PURPOSE: Instructor Analysis

import pandas as pd
from pathlib import Path

# ==================================================
# Project Paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
CHART_FOLDER = BASE_DIR / "outputs" / "charts"
REPORT_FOLDER = BASE_DIR / "outputs" / "reports"

TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# ==================================================
# Load Dataset
# ==================================================

df = pd.read_csv(PROCESSED_FOLDER / "individual_cleaned.csv")

print("Dataset loaded successfully.")

print("\n" + "=" * 70)
print("INSTRUCTOR ANALYSIS")
print("=" * 70)

print(df.info())

print("\nFirst Five Records")
print(df.head())

# ==================================================
# TRAINER FACILITATION ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("TRAINER FACILITATION ANALYSIS")
print("=" * 70)

trainer_facilitation = pd.DataFrame({

    "Average": [df["Trainer Facilitation"].mean()],
    "Median": [df["Trainer Facilitation"].median()],
    "Minimum": [df["Trainer Facilitation"].min()],
    "Maximum": [df["Trainer Facilitation"].max()],
    "Std_Deviation": [df["Trainer Facilitation"].std()]

})

print(trainer_facilitation)

trainer_facilitation.to_csv(
    TABLE_FOLDER / "trainer_facilitation_analysis.csv",
    index=False
)

print("Trainer Facilitation table saved.")

# ==================================================
# TRAINER FEEDBACK QUALITY ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("TRAINER FEEDBACK QUALITY ANALYSIS")
print("=" * 70)

trainer_feedback = pd.DataFrame({

    "Average": [df["Trainer Feedback Quality"].mean()],
    "Median": [df["Trainer Feedback Quality"].median()],
    "Minimum": [df["Trainer Feedback Quality"].min()],
    "Maximum": [df["Trainer Feedback Quality"].max()],
    "Std_Deviation": [df["Trainer Feedback Quality"].std()]

})

print(trainer_feedback)

trainer_feedback.to_csv(
    TABLE_FOLDER / "trainer_feedback_quality_analysis.csv",
    index=False
)

print("Trainer Feedback Quality table saved.")


# ==================================================
# OVERALL TRAINER PERFORMANCE SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("OVERALL TRAINER PERFORMANCE SUMMARY")
print("=" * 70)

trainer_summary = pd.DataFrame({

    "Metric": [
        "Trainer Facilitation",
        "Trainer Feedback Quality"
    ],

    "Average": [
        df["Trainer Facilitation"].mean(),
        df["Trainer Feedback Quality"].mean()
    ],

    "Median": [
        df["Trainer Facilitation"].median(),
        df["Trainer Feedback Quality"].median()
    ],

    "Minimum": [
        df["Trainer Facilitation"].min(),
        df["Trainer Feedback Quality"].min()
    ],

    "Maximum": [
        df["Trainer Facilitation"].max(),
        df["Trainer Feedback Quality"].max()
    ],

    "Std_Deviation": [
        df["Trainer Facilitation"].std(),
        df["Trainer Feedback Quality"].std()
    ]

})

print(trainer_summary)

trainer_summary.to_csv(
    TABLE_FOLDER / "trainer_performance_summary.csv",
    index=False
)

print("Trainer performance summary saved.")

# ==================================================
# INSTRUCTOR ANALYSIS REPORT
# ==================================================

report_file = REPORT_FOLDER / "instructor_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("INSTRUCTOR ANALYSIS REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Participants : {len(df)}\n\n")

    file.write("Analysis Completed\n")
    file.write("------------------------------\n")
    file.write("✓ Trainer Facilitation Analysis\n")
    file.write("✓ Trainer Feedback Quality Analysis\n")
    file.write("✓ Overall Trainer Performance Summary\n\n")

    file.write("Output Files Generated\n")
    file.write("------------------------------\n")
    file.write("✓ trainer_facilitation_analysis.csv\n")
    file.write("✓ trainer_feedback_quality_analysis.csv\n")
    file.write("✓ trainer_performance_summary.csv\n")

print("\nInstructor analysis report generated successfully.")
print(f"Report saved at : {report_file}")