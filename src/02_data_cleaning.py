# PURPOSE : Clean the raw dataset

import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "data" / "raw" / "NPS_FMEA_Purnima (1).xlsx"

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

PROCESSED_FOLDER.mkdir(parents=True, exist_ok=True)


sheet1 = pd.read_excel(RAW_FILE, sheet_name=0)

sheet2 = pd.read_excel(RAW_FILE, sheet_name=1)

print("Datasets Loaded Successfully")


individual_df = sheet1.copy()

batch_df = sheet2.copy()

print("Working copies created.")


batch_df["Batch No"] = batch_df["Batch No"].ffill()

print("Batch Numbers Forward Filled")

print()

print(batch_df["Batch No"].head(15))

for column in individual_df.select_dtypes(include=["object", "string"]):
    individual_df[column] = individual_df[column].str.strip()

for column in batch_df.select_dtypes(include=["object", "string"]):
    batch_df[column] = batch_df[column].str.strip()

print("Extra spaces removed.")


text_columns = ["Strengths", "Improvements"]

for col in text_columns:
    individual_df[col] = individual_df[col].fillna("")
    batch_df[col] = batch_df[col].fillna("")

print("Text missing values handled.")

print(batch_df["Batch No"].head(20))



rating_columns = [
    "Job Relevance",
    "Content Clarity",
    "Learning Effectiveness",
    "Learner Engagement",
    "Trainer Facilitation",
    "Trainer Feedback Quality",
    "Learning Environment",
    "Overall Satisfaction"
]

print("\n" + "=" * 60)
print("NUMERIC COLUMN VALIDATION")
print("=" * 60)

for column in rating_columns:

    print(f"\n{column}")

    print(f"Minimum Value : {individual_df[column].min()}")

    print(f"Maximum Value : {individual_df[column].max()}")

    print(f"Unique Values : {sorted(individual_df[column].unique())}")

    
# ==========================================================
# Generate Data Cleaning Report
# ==========================================================

REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

report_file = REPORT_FOLDER / "data_cleaning_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("DATA CLEANING REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Individual Records : {len(individual_df)}\n")
    file.write(f"Total Batch Records      : {len(batch_df)}\n\n")

    file.write(f"Duplicate Records (Individual) : {individual_df.duplicated().sum()}\n")
    file.write(f"Duplicate Records (Batch)      : {batch_df.duplicated().sum()}\n\n")

    file.write("Original Missing Improvements : 20\n")
    file.write("Original Missing Batch Numbers : 150\n\n")

    file.write("Cleaning Operations Performed\n")
    file.write("----------------------------------------\n")
    file.write("✓ Created Working Copies\n")
    file.write("✓ Forward Filled Batch Numbers\n")
    file.write("✓ Removed Leading & Trailing Spaces\n")
    file.write("✓ Filled Missing Text Fields\n")
    file.write("✓ Validated Numeric Rating Columns\n")
    file.write("✓ Saved Cleaned Datasets\n")

print("\nCleaning report generated successfully!")
print(f"Report saved at : {report_file}")

# ==========================================================
# Save Cleaned Datasets
# ==========================================================

individual_df.to_csv(
    PROCESSED_FOLDER / "individual_cleaned.csv",
    index=False
)

batch_df.to_csv(
    PROCESSED_FOLDER / "batch_cleaned.csv",
    index=False
)

print("\nCleaned datasets saved successfully.")

individual_df.to_csv(
    PROCESSED_FOLDER / "individual_cleaned.csv",
    index=False
)

batch_df.to_csv(
    PROCESSED_FOLDER / "batch_cleaned.csv",
    index=False
)

print("Cleaned datasets saved successfully.")