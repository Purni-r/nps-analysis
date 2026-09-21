# PURPOSE : Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

CHART_FOLDER = BASE_DIR / "outputs" / "charts"
REPORT_FOLDER = BASE_DIR / "outputs" / "reports"

CHART_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)


individual_df = pd.read_csv(PROCESSED_FOLDER / "individual_featured.csv")

batch_df = pd.read_csv(PROCESSED_FOLDER / "batch_featured.csv")

print("Datasets Loaded Successfully")

# DATASET SUMMARY

print("\n" + "="*70)
print("INDIVIDUAL DATASET")
print("="*70)

print(individual_df.info())

print("\n")

print(individual_df.describe(include="all"))

# MISSING VALUES

print("\n" + "="*70)
print("MISSING VALUES")
print("="*70)

print(individual_df.isnull().sum())

# DUPLICATE RECORDS

print("\n" + "="*70)
print("DUPLICATE RECORDS")
print("="*70)

print("Duplicates :", individual_df.duplicated().sum())

# NPS DISTRIBUTION

plt.figure(figsize=(7,5))

individual_df["NPS"].value_counts().sort_index().plot(kind="bar")

plt.title("NPS Distribution")

plt.xlabel("NPS")

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(CHART_FOLDER/"nps_distribution.png")

plt.close()

print("NPS Distribution Chart Saved")

plt.figure(figsize=(8,5))

individual_df["Age_Group"].value_counts().plot(kind="bar")

plt.title("Age Group Distribution")

plt.tight_layout()

plt.savefig(CHART_FOLDER/"age_group_distribution.png")

plt.close()

print("Age Group Chart Saved")


plt.figure(figsize=(8,5))

individual_df["Experience_Group"].value_counts().plot(kind="bar")

plt.title("Experience Group Distribution")

plt.tight_layout()

plt.savefig(CHART_FOLDER/"experience_group_distribution.png")

plt.close()

print("Experience Group Chart Saved")

plt.figure(figsize=(6,6))

individual_df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Gender Distribution")

plt.savefig(CHART_FOLDER/"gender_distribution.png")

plt.close()

print("Gender Chart Saved")

plt.figure(figsize=(6,6))

individual_df["Martial status"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Marital Status Distribution")

plt.savefig(CHART_FOLDER/"marital_status_distribution.png")

plt.close()

print("Marital Status Chart Saved")

# EDA REPORT

report = REPORT_FOLDER / "EDA_Report.txt"

with open(report, "w", encoding="utf-8") as file:

    file.write("="*60 + "\n")
    file.write("EXPLORATORY DATA ANALYSIS REPORT\n")
    file.write("="*60 + "\n\n")

    file.write(f"Total Participants : {len(individual_df)}\n")
    file.write(f"Total Variables : {individual_df.shape[1]}\n\n")

    file.write("NPS Distribution\n")
    file.write(str(individual_df["NPS"].value_counts()))
    file.write("\n\n")

    file.write("Gender Distribution\n")
    file.write(str(individual_df["Gender"].value_counts()))
    file.write("\n\n")

    file.write("Marital Status Distribution\n")
    file.write(str(individual_df["Martial status"].value_counts()))
    file.write("\n\n")

    file.write("Age Group Distribution\n")
    file.write(str(individual_df["Age_Group"].value_counts()))
    file.write("\n\n")

    file.write("Experience Group Distribution\n")
    file.write(str(individual_df["Experience_Group"].value_counts()))

print("EDA Report Generated Successfully")

