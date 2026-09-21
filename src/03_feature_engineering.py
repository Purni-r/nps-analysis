# PURPOSE : Create engineered features

import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

REPORT_FOLDER = BASE_DIR / "outputs" / "reports"

REPORT_FOLDER.mkdir(parents=True, exist_ok=True)


individual_df = pd.read_csv(PROCESSED_FOLDER / "individual_cleaned.csv")

batch_df = pd.read_csv(PROCESSED_FOLDER / "batch_cleaned.csv")

print("Cleaned datasets loaded successfully.")

# Create Participant ID

individual_df.insert(
    0,
    "Participant_ID",
    [f"P{str(i).zfill(3)}" for i in range(1, len(individual_df) + 1)]
)

batch_df.insert(
    0,
    "Participant_ID",
    [f"P{str(i).zfill(3)}" for i in range(1, len(batch_df) + 1)]
)

print("Participant IDs created successfully.")

print("\nFirst Five Participant IDs\n")

print(individual_df[["Participant_ID"]].head())


# Inspect Age and Experience Values

print("\n" + "=" * 60)
print("AGE COLUMN SAMPLE")
print("=" * 60)

print(individual_df["Age"].head(10))

print("\n" + "=" * 60)
print("EXPERIENCE COLUMN SAMPLE")
print("=" * 60)

print(individual_df["Experience"].head(10))


import re

def convert_to_years_and_months(duration):

    if pd.isna(duration):
        return pd.Series([None, None])

    pattern = r"(\d+)\s+years\s+(\d+)\s+months\s+(\d+)\s+days"

    match = re.match(pattern, str(duration).strip())

    if match:

        years = int(match.group(1))
        months = int(match.group(2))
        days = int(match.group(3))

        total_years = years + (months / 12) + (days / 365)

        total_months = (years * 12) + months + (days / 30)

        return pd.Series([
            round(total_years, 2),
            round(total_months, 2)
        ])

    return pd.Series([None, None])


individual_df[
    ["Age_Years", "Age_Months"]
] = individual_df["Age"].apply(convert_to_years_and_months)

batch_df[
    ["Age_Years", "Age_Months"]
] = batch_df["Age"].apply(convert_to_years_and_months)

print("Age features created successfully.")


individual_df[
    ["Experience_Years", "Experience_Months"]
] = individual_df["Experience"].apply(convert_to_years_and_months)

batch_df[
    ["Experience_Years", "Experience_Months"]
] = batch_df["Experience"].apply(convert_to_years_and_months)

print("Experience features created successfully.")


print("\n")
print("=" * 70)
print("NUMERIC FEATURE ENGINEERING")
print("=" * 70)

print(
    individual_df[
        [
            "Age",
            "Age_Years",
            "Age_Months",
            "Experience",
            "Experience_Years",
            "Experience_Months"
        ]
    ].head(10)
)

# Age and Experience Summary


print("\n" + "=" * 70)
print("AGE SUMMARY")
print("=" * 70)

print(individual_df["Age_Years"].describe())

print("\n" + "=" * 70)
print("EXPERIENCE SUMMARY")
print("=" * 70)

print(individual_df["Experience_Years"].describe())



def age_group(age):

    if age <= 25:
        return "20-25 (Early Career)"

    elif age <= 30:
        return "26-30 (Young Professional)"

    elif age <= 35:
        return "31-35 (Mid Career)"

    elif age <= 40:
        return "36-40 (Senior Professional)"

    else:
        return "40+ (Highly Experienced)"


individual_df["Age_Group"] = individual_df["Age_Years"].apply(age_group)

batch_df["Age_Group"] = batch_df["Age_Years"].apply(age_group)

print("Age groups created successfully.")


def experience_group(exp):

    if exp <= 2:
        return "0-2 Years (Beginner)"

    elif exp <= 5:
        return "2-5 Years (Junior)"

    elif exp <= 10:
        return "5-10 Years (Intermediate)"

    elif exp <= 20:
        return "10-20 Years (Senior)"

    else:
        return "20+ Years (Expert)"


individual_df["Experience_Group"] = individual_df["Experience_Years"].apply(experience_group)

batch_df["Experience_Group"] = batch_df["Experience_Years"].apply(experience_group)

print("Experience groups created successfully.")


print("\n" + "=" * 70)
print("AGE GROUP DISTRIBUTION")
print("=" * 70)

print(individual_df["Age_Group"].value_counts().sort_index())

print("\n" + "=" * 70)
print("EXPERIENCE GROUP DISTRIBUTION")
print("=" * 70)

print(individual_df["Experience_Group"].value_counts().sort_index())


print("\n" + "=" * 70)
print("NPS VALUE DISTRIBUTION")
print("=" * 70)

print("Minimum NPS :", individual_df["NPS"].min())
print("Maximum NPS :", individual_df["NPS"].max())

print("\nUnique NPS Values")

print(sorted(individual_df["NPS"].unique()))


# Content Quality Index
individual_df["Content_Quality_Index"] = (
    individual_df["Job Relevance"] +
    individual_df["Content Clarity"] +
    individual_df["Learning Effectiveness"]
) / 3

batch_df["Content_Quality_Index"] = (
    batch_df["Job Relevance"] +
    batch_df["Content Clarity"] +
    batch_df["Learning Effectiveness"]
) / 3


# Trainer Effectiveness Index
individual_df["Trainer_Effectiveness_Index"] = (
    individual_df["Trainer Facilitation"] +
    individual_df["Trainer Feedback Quality"] +
    individual_df["Learner Engagement"]
) / 3

batch_df["Trainer_Effectiveness_Index"] = (
    batch_df["Trainer Facilitation"] +
    batch_df["Trainer Feedback Quality"] +
    batch_df["Learner Engagement"]
) / 3


# Learning Environment Index
individual_df["Learning_Environment_Index"] = (
    individual_df["Learning Environment"] +
    individual_df["Overall Satisfaction"]
) / 2

batch_df["Learning_Environment_Index"] = (
    batch_df["Learning Environment"] +
    batch_df["Overall Satisfaction"]
) / 2

print("Composite indices created successfully.")

print("\n" + "="*70)
print("COMPOSITE INDICES")
print("="*70)

print(individual_df[
    [
        "Content_Quality_Index",
        "Trainer_Effectiveness_Index",
        "Learning_Environment_Index"
    ]
].head())


def nps_category(score):

    if score >= 9:
        return "Promoter"
    else:
        return "Passive"


individual_df["NPS_Category"] = individual_df["NPS"].apply(nps_category)
batch_df["NPS_Category"] = batch_df["NPS"].apply(nps_category)

print("NPS Category created successfully.")



individual_df["Is_Promoter"] = (individual_df["NPS"] >= 9).astype(int)
individual_df["Is_Passive"] = (individual_df["NPS"] <= 8).astype(int)

batch_df["Is_Promoter"] = (batch_df["NPS"] >= 9).astype(int)
batch_df["Is_Passive"] = (batch_df["NPS"] <= 8).astype(int)

print("Binary NPS features created successfully.")

print("\n" + "="*70)
print("NPS FEATURE DISTRIBUTION")
print("="*70)

print(individual_df["NPS_Category"].value_counts())

print("\n")

print(individual_df[
    [
        "NPS",
        "NPS_Category",
        "Is_Promoter",
        "Is_Passive"
    ]
].head(10))

# ==========================================================
# SAVE FEATURE ENGINEERED DATASETS
# ==========================================================

individual_df.to_csv(
    PROCESSED_FOLDER / "individual_featured.csv",
    index=False
)

batch_df.to_csv(
    PROCESSED_FOLDER / "batch_featured.csv",
    index=False
)

print("\nFeature engineered datasets saved successfully.")

# ==========================================================
# FEATURE ENGINEERING REPORT
# ==========================================================

report_file = REPORT_FOLDER / "feature_engineering_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 60 + "\n")
    file.write("FEATURE ENGINEERING REPORT\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Total Participants : {len(individual_df)}\n\n")

    file.write("Features Created\n")
    file.write("-----------------------------\n")
    file.write("✓ Participant_ID\n")
    file.write("✓ Age_Years\n")
    file.write("✓ Age_Months\n")
    file.write("✓ Experience_Years\n")
    file.write("✓ Experience_Months\n")
    file.write("✓ Age_Group\n")
    file.write("✓ Experience_Group\n")
    file.write("✓ Content_Quality_Index\n")
    file.write("✓ Trainer_Effectiveness_Index\n")
    file.write("✓ Learning_Environment_Index\n")
    file.write("✓ NPS_Category\n")
    file.write("✓ Is_Promoter\n")
    file.write("✓ Is_Passive\n")

print("\nFeature engineering report generated successfully.")
print(f"Report saved at : {report_file}")