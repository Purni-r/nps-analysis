# PURPOSE: Load and inspect the Excel dataset


import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "NPS_FMEA_Purnima (1).xlsx"

PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed"

PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)



print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

sheet1 = pd.read_excel(RAW_DATA_PATH, sheet_name=0)

sheet2 = pd.read_excel(RAW_DATA_PATH, sheet_name=1)

print("\nDataset Loaded Successfully!")

print(f"\nSheet 1 Shape : {sheet1.shape}")

print(f"Sheet 2 Shape : {sheet2.shape}")


# Basic Dataset Information


print("\n")
print("=" * 60)
print("SHEET 1 INFORMATION")
print("=" * 60)

print(sheet1.info())

print("\n")
print("=" * 60)
print("SHEET 2 INFORMATION")
print("=" * 60)

print(sheet2.info())


print("\n")
print("=" * 60)
print("SHEET 1 PREVIEW")
print("=" * 60)

print(sheet1.head())

print("\n")
print("=" * 60)
print("SHEET 2 PREVIEW")
print("=" * 60)

print(sheet2.head())

def load_data():
    ...

def inspect_data():
    ...

def save_data():
    ...

def main():
    ...
    
# Missing Value Analysis


print("\n")
print("=" * 60)
print("MISSING VALUE ANALYSIS")
print("=" * 60)

print("\nSheet 1 Missing Values\n")

missing_sheet1 = sheet1.isnull().sum()

print(missing_sheet1)

print("\n")

print("Sheet 2 Missing Values\n")

missing_sheet2 = sheet2.isnull().sum()

print(missing_sheet2)


print("\n")
print("=" * 60)
print("MISSING VALUE PERCENTAGE")
print("=" * 60)

missing_percent_sheet1 = (sheet1.isnull().sum() / len(sheet1)) * 100

missing_percent_sheet2 = (sheet2.isnull().sum() / len(sheet2)) * 100

print("\nSheet 1")

print(missing_percent_sheet1.round(2))

print("\nSheet 2")

print(missing_percent_sheet2.round(2))

# Duplicate Analysis


print("\n")
print("=" * 60)
print("DUPLICATE ANALYSIS")
print("=" * 60)

duplicates_sheet1 = sheet1.duplicated().sum()

duplicates_sheet2 = sheet2.duplicated().sum()

print(f"\nSheet 1 Duplicate Rows : {duplicates_sheet1}")

print(f"Sheet 2 Duplicate Rows : {duplicates_sheet2}")

# Unique Values

categorical_columns = [

    "Age",

    "Experience",

    "Designation",

    "Dept",

    "Role",

    "Region",

    "Martial status",

    "Gender"

]

print("\n")
print("=" * 60)
print("UNIQUE VALUES")
print("=" * 60)

for column in categorical_columns:

    print(f"\n{column}")

    print("-" * 30)

    print(sheet1[column].unique())

print("\n")
print("=" * 60)
print("CATEGORY COUNTS")
print("=" * 60)

for column in categorical_columns:

    print(f"\n{column}")

    print(sheet1[column].value_counts())

    print("-" * 40)


