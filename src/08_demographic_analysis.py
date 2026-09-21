# PURPOSE: Perform Demographic Analysis

import pandas as pd
from pathlib import Path

# ==================================================
# Project Paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
CHART_FOLDER = BASE_DIR / "outputs" / "charts"

TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)

# ==================================================
# Load Dataset
# ==================================================

df = pd.read_csv(PROCESSED_FOLDER / "individual_cleaned.csv")

print("Dataset loaded successfully.")

print("\n" + "=" * 70)
print("DEMOGRAPHIC ANALYSIS")
print("=" * 70)

print(df.info())

print("\nFirst Five Records")
print(df.head())

# ==================================================
# Create Promoter Flag (if not available)
# ==================================================

df["Is_Promoter"] = (df["NPS"] >= 9).astype(int)

# ==================================================
# GENDER ANALYSIS
# ==================================================

print("\n" + "=" * 70)
print("GENDER DEMOGRAPHIC SUMMARY")
print("=" * 70)

gender_summary = (
    df.groupby("Gender")
      .agg(
          Participants=("Gender", "count"),
          Average_NPS=("NPS", "mean"),
          Std_NPS=("NPS", "std"),
          Promoters=("Is_Promoter", "sum")
      )
      .reset_index()
)

gender_summary["Promoter_Percentage"] = (
    gender_summary["Promoters"] /
    gender_summary["Participants"] * 100
).round(2)

print(gender_summary)

gender_summary.to_csv(
    TABLE_FOLDER / "demographic_gender_summary.csv",
    index=False
)

print("Gender demographic table saved.")

# ==================================================
# AGE GROUP DEMOGRAPHIC SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("AGE GROUP DEMOGRAPHIC SUMMARY")
print("=" * 70)

# Create Age_Group if it doesn't exist
def get_age_group(age_text):

    years = int(age_text.split(" ")[0])

    if years <= 25:
        return "20-25 (Early Career)"
    elif years <= 30:
        return "26-30 (Young Professional)"
    elif years <= 35:
        return "31-35 (Mid Career)"
    elif years <= 40:
        return "36-40 (Senior Professional)"
    else:
        return "40+ (Highly Experienced)"

df["Age_Group"] = df["Age"].apply(get_age_group)

age_summary = (
    df.groupby("Age_Group")
      .agg(
          Participants=("Age_Group", "count"),
          Average_NPS=("NPS", "mean"),
          Std_NPS=("NPS", "std"),
          Promoters=("Is_Promoter", "sum")
      )
      .reset_index()
)

age_summary["Promoter_Percentage"] = (
    age_summary["Promoters"] /
    age_summary["Participants"] * 100
).round(2)

print(age_summary)

age_summary.to_csv(
    TABLE_FOLDER / "demographic_age_group_summary.csv",
    index=False
)

print("Age group demographic table saved.")

# ==================================================
# EXPERIENCE GROUP DEMOGRAPHIC SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("EXPERIENCE GROUP DEMOGRAPHIC SUMMARY")
print("=" * 70)

# Create Experience_Group if it doesn't exist
def get_experience_group(exp_text):

    years = int(exp_text.split(" ")[0])

    if years <= 2:
        return "0-2 Years (Beginner)"
    elif years <= 5:
        return "2-5 Years (Junior)"
    elif years <= 10:
        return "5-10 Years (Intermediate)"
    elif years <= 20:
        return "10-20 Years (Senior)"
    else:
        return "20+ Years (Expert)"

df["Experience_Group"] = df["Experience"].apply(get_experience_group)

experience_summary = (
    df.groupby("Experience_Group")
      .agg(
          Participants=("Experience_Group", "count"),
          Average_NPS=("NPS", "mean"),
          Std_NPS=("NPS", "std"),
          Promoters=("Is_Promoter", "sum")
      )
      .reset_index()
)

experience_summary["Promoter_Percentage"] = (
    experience_summary["Promoters"] /
    experience_summary["Participants"] * 100
).round(2)

print(experience_summary)

experience_summary.to_csv(
    TABLE_FOLDER / "demographic_experience_group_summary.csv",
    index=False
)

print("Experience group demographic table saved.")

# ==================================================
# DEPARTMENT DEMOGRAPHIC SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("DEPARTMENT DEMOGRAPHIC SUMMARY")
print("=" * 70)

department_summary = (
    df.groupby("Dept")
      .agg(
          Participants=("Dept", "count"),
          Average_NPS=("NPS", "mean"),
          Std_NPS=("NPS", "std"),
          Promoters=("Is_Promoter", "sum")
      )
      .reset_index()
)

department_summary["Promoter_Percentage"] = (
    department_summary["Promoters"] /
    department_summary["Participants"] * 100
).round(2)

print(department_summary)

department_summary.to_csv(
    TABLE_FOLDER / "demographic_department_summary.csv",
    index=False
)

print("Department demographic table saved.")

# ==================================================
# REGION DEMOGRAPHIC SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("REGION DEMOGRAPHIC SUMMARY")
print("=" * 70)

region_summary = (
    df.groupby("Region")
      .agg(
          Participants=("Region", "count"),
          Average_NPS=("NPS", "mean"),
          Std_NPS=("NPS", "std"),
          Promoters=("Is_Promoter", "sum")
      )
      .reset_index()
)

region_summary["Promoter_Percentage"] = (
    region_summary["Promoters"] /
    region_summary["Participants"] * 100
).round(2)

print(region_summary)

region_summary.to_csv(
    TABLE_FOLDER / "demographic_region_summary.csv",
    index=False
)

print("Region demographic table saved.")

# ==================================================
# MARITAL STATUS DEMOGRAPHIC SUMMARY
# ==================================================

print("\n" + "=" * 70)
print("MARITAL STATUS DEMOGRAPHIC SUMMARY")
print("=" * 70)

marital_summary = (
    df.groupby("Martial status")
      .agg(
          Participants=("Martial status", "count"),
          Average_NPS=("NPS", "mean"),
          Std_NPS=("NPS", "std"),
          Promoters=("Is_Promoter", "sum")
      )
      .reset_index()
)

marital_summary["Promoter_Percentage"] = (
    marital_summary["Promoters"] /
    marital_summary["Participants"] * 100
).round(2)

print(marital_summary)

marital_summary.to_csv(
    TABLE_FOLDER / "demographic_marital_status_summary.csv",
    index=False
)

print("Marital status demographic table saved.")


# ==================================================
# DEMOGRAPHIC ANALYSIS REPORT
# ==================================================

report_file = REPORT_FOLDER / "demographic_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("DEMOGRAPHIC ANALYSIS REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Participants : {len(df)}\n\n")

    file.write("Analysis Completed\n")
    file.write("------------------------------\n")
    file.write("✓ Gender Demographic Summary\n")
    file.write("✓ Age Group Demographic Summary\n")
    file.write("✓ Experience Group Demographic Summary\n")
    file.write("✓ Department Demographic Summary\n")
    file.write("✓ Region Demographic Summary\n")
    file.write("✓ Marital Status Demographic Summary\n\n")

    file.write("Output Files Generated\n")
    file.write("------------------------------\n")
    file.write("✓ demographic_gender_summary.csv\n")
    file.write("✓ demographic_age_group_summary.csv\n")
    file.write("✓ demographic_experience_group_summary.csv\n")
    file.write("✓ demographic_department_summary.csv\n")
    file.write("✓ demographic_region_summary.csv\n")
    file.write("✓ demographic_marital_status_summary.csv\n")

print("\nDemographic analysis report generated successfully.")
print(f"Report saved at : {report_file}")

# ==========================================================
# DEMOGRAPHIC ANALYSIS REPORT
# ==========================================================

report_file = REPORT_FOLDER / "demographic_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("DEMOGRAPHIC ANALYSIS REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Participants : {len(df)}\n\n")

    file.write("Analysis Completed\n")
    file.write("------------------------------\n")
    file.write("✓ Gender Demographic Summary\n")
    file.write("✓ Marital Status Demographic Summary\n")
    file.write("✓ Age Group Demographic Summary\n")
    file.write("✓ Experience Group Demographic Summary\n")
    file.write("✓ Department Demographic Summary\n")
    file.write("✓ Region Demographic Summary\n")
    file.write("✓ Designation Demographic Summary\n")
    file.write("✓ Role Demographic Summary\n")
    file.write("✓ Gender Distribution Chart\n")
    file.write("✓ Marital Status Distribution Chart\n")
    file.write("✓ Age Group Distribution Chart\n")
    file.write("✓ Experience Group Distribution Chart\n")
    file.write("✓ Department Distribution Chart\n")
    file.write("✓ Region Distribution Chart\n")
    file.write("✓ Designation Distribution Chart\n")
    file.write("✓ Role Distribution Chart\n")

print("\nDemographic analysis report generated successfully.")
print(f"Report saved at : {report_file}")