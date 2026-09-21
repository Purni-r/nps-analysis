# PURPOSE: Statistical Analysis

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
print("STATISTICAL ANALYSIS")
print("=" * 70)

print(df.info())

print("\nFirst Five Records")
print(df.head())

# ==================================================
# DESCRIPTIVE STATISTICS
# ==================================================

print("\n" + "=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

statistics = df[[
    "NPS",
    "Job Relevance",
    "Content Clarity",
    "Learning Effectiveness",
    "Learner Engagement",
    "Trainer Facilitation",
    "Trainer Feedback Quality",
    "Learning Environment",
    "Overall Satisfaction"
]].describe()

print(statistics)

statistics.to_csv(
    TABLE_FOLDER / "descriptive_statistics.csv"
)

print("Descriptive statistics saved.")

# ==========================================================
# CORRELATION ANALYSIS
# ==========================================================

print("\n" + "=" * 70)
print("CORRELATION ANALYSIS")
print("=" * 70)

correlation_columns = [

    "NPS",
    "Job Relevance",
    "Content Clarity",
    "Learning Effectiveness",
    "Learner Engagement",
    "Trainer Facilitation",
    "Trainer Feedback Quality",
    "Learning Environment",
    "Overall Satisfaction"

]

correlation_matrix = df[correlation_columns].corr()

print(correlation_matrix)

correlation_matrix.to_csv(
    TABLE_FOLDER / "correlation_analysis.csv"
)

print("Correlation analysis saved.")

from scipy.stats import ttest_ind

# ==========================================================
# HYPOTHESIS TESTING
# ==========================================================

print("\n" + "=" * 70)
print("HYPOTHESIS TESTING")
print("=" * 70)

male_nps = df[df["Gender"] == "Male"]["NPS"]

female_nps = df[df["Gender"] == "Female"]["NPS"]

t_statistic, p_value = ttest_ind(
    male_nps,
    female_nps,
    equal_var=False
)

print(f"T-Statistic : {t_statistic:.4f}")
print(f"P-Value     : {p_value:.4f}")

if p_value < 0.05:
    result = "Significant Difference"
else:
    result = "No Significant Difference"

print(f"Conclusion  : {result}")

hypothesis_result = pd.DataFrame({

    "T_Statistic": [round(t_statistic, 4)],
    "P_Value": [round(p_value, 4)],
    "Conclusion": [result]

})

hypothesis_result.to_csv(
    TABLE_FOLDER / "hypothesis_testing.csv",
    index=False
)

print("Hypothesis testing results saved.")

# ==========================================================
# STATISTICAL ANALYSIS REPORT
# ==========================================================

report_file = REPORT_FOLDER / "statistical_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("STATISTICAL ANALYSIS REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Participants : {len(df)}\n\n")

    file.write("Analysis Completed\n")
    file.write("------------------------------\n")
    file.write("✓ Descriptive Statistics\n")
    file.write("✓ Correlation Analysis\n")
    file.write("✓ Hypothesis Testing\n\n")

    file.write("Output Files Generated\n")
    file.write("------------------------------\n")
    file.write("✓ descriptive_statistics.csv\n")
    file.write("✓ correlation_analysis.csv\n")
    file.write("✓ hypothesis_testing.csv\n")

print("\nStatistical analysis report generated successfully.")
print(f"Report saved at : {report_file}")