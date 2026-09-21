# PURPOSE: Text Analysis

import pandas as pd
from pathlib import Path

# ==================================================
# Project Paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
REPORT_FOLDER = BASE_DIR / "outputs" / "reports"

TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# ==================================================
# Load Dataset
# ==================================================

df = pd.read_csv(PROCESSED_FOLDER / "individual_cleaned.csv")

print("Dataset loaded successfully.")

print("\n" + "=" * 70)
print("TEXT ANALYSIS")
print("=" * 70)

print(df.info())

print("\nFirst Five Records")
print(df.head())

# ==================================================
# STRENGTHS SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("STRENGTHS SUMMARY")
print("=" * 70)

strength_summary = pd.DataFrame({

    "Total_Responses": [df["Strengths"].notna().sum()],
    "Unique_Responses": [df["Strengths"].nunique()],
    "Empty_Responses": [(df["Strengths"].fillna("").str.strip() == "").sum()]

})

print(strength_summary)

strength_summary.to_csv(
    TABLE_FOLDER / "strengths_summary.csv",
    index=False
)

print("Strengths summary saved.")

# ==================================================
# IMPROVEMENTS SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("IMPROVEMENTS SUMMARY")
print("=" * 70)

improvement_summary = pd.DataFrame({

    "Total_Responses": [df["Improvements"].notna().sum()],
    "Unique_Responses": [df["Improvements"].nunique()],
    "Empty_Responses": [(df["Improvements"].fillna("").str.strip() == "").sum()]

})

print(improvement_summary)

improvement_summary.to_csv(
    TABLE_FOLDER / "improvements_summary.csv",
    index=False
)

print("Improvements summary saved.")

# ==================================================
# MOST COMMON STRENGTHS
# ==================================================

print("\n" + "=" * 70)
print("MOST COMMON STRENGTHS")
print("=" * 70)

common_strengths = (
    df["Strengths"]
    .fillna("No Response")
    .value_counts()
    .head(10)
    .reset_index()
)

common_strengths.columns = ["Strength", "Count"]

print(common_strengths)

common_strengths.to_csv(
    TABLE_FOLDER / "most_common_strengths.csv",
    index=False
)

print("Most common strengths table saved.")

# ==================================================
# MOST COMMON IMPROVEMENTS
# ==================================================

print("\n" + "=" * 70)
print("MOST COMMON IMPROVEMENTS")
print("=" * 70)

common_improvements = (
    df["Improvements"]
    .fillna("No Response")
    .replace("", "No Response")
    .value_counts()
    .head(10)
    .reset_index()
)

common_improvements.columns = ["Improvement", "Count"]

print(common_improvements)

common_improvements.to_csv(
    TABLE_FOLDER / "most_common_improvements.csv",
    index=False
)

print("Most common improvements table saved.")

# ==================================================
# TEXT ANALYSIS REPORT
# ==================================================

report_file = REPORT_FOLDER / "text_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("TEXT ANALYSIS REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Participants : {len(df)}\n\n")

    file.write("Analysis Completed\n")
    file.write("------------------------------\n")
    file.write("✓ Strengths Summary\n")
    file.write("✓ Improvements Summary\n")
    file.write("✓ Most Common Strengths\n")
    file.write("✓ Most Common Improvements\n\n")

    file.write("Output Files Generated\n")
    file.write("------------------------------\n")
    file.write("✓ strengths_summary.csv\n")
    file.write("✓ improvements_summary.csv\n")
    file.write("✓ most_common_strengths.csv\n")
    file.write("✓ most_common_improvements.csv\n")

print("\nText analysis report generated successfully.")
print(f"Report saved at : {report_file}")