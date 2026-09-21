# PURPOSE : Individual NPS Analysis

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
CHART_FOLDER = BASE_DIR / "outputs" / "charts"

REPORT_FOLDER.mkdir(parents=True, exist_ok=True)
TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)


individual_df = pd.read_csv(
    PROCESSED_FOLDER / "individual_featured.csv"
)

print("Individual dataset loaded successfully.")

# OVERALL NPS SUMMARY

print("\n" + "="*70)
print("OVERALL NPS SUMMARY")
print("="*70)

total_participants = len(individual_df)

promoters = individual_df["Is_Promoter"].sum()

passives = individual_df["Is_Passive"].sum()

promoter_percentage = (promoters / total_participants) * 100

passive_percentage = (passives / total_participants) * 100

average_nps = individual_df["NPS"].mean()

print(f"Total Participants : {total_participants}")
print(f"Promoters          : {promoters}")
print(f"Passives           : {passives}")
print(f"Average NPS        : {average_nps:.2f}")
print(f"Promoter %         : {promoter_percentage:.2f}%")
print(f"Passive %          : {passive_percentage:.2f}%")


# OVERALL NPS CHART

summary = pd.Series({
    "Promoters": promoters,
    "Passives": passives
})

plt.figure(figsize=(6,5))

summary.plot(kind="bar")

plt.title("Overall NPS Category Distribution")

plt.ylabel("Participants")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "overall_nps_summary.png"
)

plt.close()

print("Overall NPS chart saved.")

# SAVE SUMMARY TABLE

summary_df = pd.DataFrame({

    "Metric": [

        "Total Participants",

        "Promoters",

        "Passives",

        "Average NPS",

        "Promoter Percentage",

        "Passive Percentage"

    ],

    "Value": [

        total_participants,

        promoters,

        passives,

        round(average_nps,2),

        round(promoter_percentage,2),

        round(passive_percentage,2)

    ]

})

summary_df.to_csv(

    TABLE_FOLDER / "overall_nps_summary.csv",

    index=False

)

print("Overall summary table saved.")

# DEPARTMENT ANALYSIS

department_summary = (
    individual_df.groupby("Dept")
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

department_summary["Promoter_Percentage"] = (
    department_summary["Promoters"] /
    department_summary["Participants"] * 100
)

department_summary = department_summary.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("DEPARTMENT ANALYSIS")
print("=" * 70)

print(department_summary)


department_summary.to_csv(
    TABLE_FOLDER / "department_analysis.csv",
    index=False
)

print("Department analysis table saved.")

plt.figure(figsize=(10,6))

department_summary.plot(
    x="Dept",
    y="Average_NPS",
    kind="bar",
    legend=False
)

plt.title("Average NPS by Department")
plt.xlabel("Department")
plt.ylabel("Average NPS")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "department_analysis.png"
)

plt.close()

print("Department chart saved.")


# REGION ANALYSIS

region_analysis = (
    individual_df
    .groupby("Region")
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

region_analysis["Promoter_Percentage"] = (
    region_analysis["Promoters"]
    / region_analysis["Participants"]
) * 100

region_analysis = region_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("REGION ANALYSIS")
print("=" * 70)

print(region_analysis)

region_analysis.to_csv(
    TABLE_FOLDER / "region_analysis.csv",
    index=False
)

print("Region analysis table saved.")

plt.figure(figsize=(10,5))

plt.bar(
    region_analysis["Region"],
    region_analysis["Average_NPS"]
)

plt.title("Average NPS by Region")

plt.xlabel("Region")

plt.ylabel("Average NPS")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "region_analysis.png"
)

plt.close()

print("Region chart saved.")


# ROLE ANALYSIS

role_analysis = (
    individual_df
    .groupby("Role")
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

role_analysis["Promoter_Percentage"] = (
    role_analysis["Promoters"]
    / role_analysis["Participants"]
) * 100

role_analysis = role_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("ROLE ANALYSIS")
print("=" * 70)

print(role_analysis)

role_analysis.to_csv(
    TABLE_FOLDER / "role_analysis.csv",
    index=False
)

print("Role analysis table saved.")

plt.figure(figsize=(10,5))

plt.bar(
    role_analysis["Role"],
    role_analysis["Average_NPS"]
)

plt.title("Average NPS by Role")

plt.xlabel("Role")

plt.ylabel("Average NPS")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "role_analysis.png"
)

plt.close()

print("Role chart saved.")


# GENDER ANALYSIS

gender_analysis = (
    individual_df
    .groupby("Gender")
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

gender_analysis["Promoter_Percentage"] = (
    gender_analysis["Promoters"]
    / gender_analysis["Participants"]
) * 100

gender_analysis = gender_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("GENDER ANALYSIS")
print("=" * 70)

print(gender_analysis)

gender_analysis.to_csv(
    TABLE_FOLDER / "gender_analysis.csv",
    index=False
)

print("Gender analysis table saved.")

plt.figure(figsize=(6,5))

plt.bar(
    gender_analysis["Gender"],
    gender_analysis["Average_NPS"]
)

plt.title("Average NPS by Gender")

plt.xlabel("Gender")

plt.ylabel("Average NPS")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "gender_analysis.png"
)

plt.close()

print("Gender chart saved.")


# MARITAL STATUS ANALYSIS

marital_analysis = (
    individual_df
    .groupby("Martial status")
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

marital_analysis["Promoter_Percentage"] = (
    marital_analysis["Promoters"]
    / marital_analysis["Participants"]
) * 100

marital_analysis = marital_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("MARITAL STATUS ANALYSIS")
print("=" * 70)

print(marital_analysis)

marital_analysis.to_csv(
    TABLE_FOLDER / "marital_status_analysis.csv",
    index=False
)

print("Marital status analysis table saved.")

plt.figure(figsize=(6,5))

plt.bar(
    marital_analysis["Martial status"],
    marital_analysis["Average_NPS"]
)

plt.title("Average NPS by Marital Status")

plt.xlabel("Marital Status")

plt.ylabel("Average NPS")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "marital_status_analysis.png"
)

plt.close()

print("Marital status chart saved.")

# AGE GROUP ANALYSIS


age_analysis = (
    individual_df
    .groupby("Age_Group")
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

age_analysis["Promoter_Percentage"] = (
    age_analysis["Promoters"]
    / age_analysis["Participants"]
) * 100

age_analysis = age_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("AGE GROUP ANALYSIS")
print("=" * 70)

print(age_analysis)

age_analysis.to_csv(
    TABLE_FOLDER / "age_group_analysis.csv",
    index=False
)

print("Age group analysis table saved.")

plt.figure(figsize=(10,5))

plt.bar(
    age_analysis["Age_Group"],
    age_analysis["Average_NPS"]
)

plt.title("Average NPS by Age Group")

plt.xlabel("Age Group")

plt.ylabel("Average NPS")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "age_group_analysis.png"
)

plt.close()

print("Age group chart saved.")

# EXPERIENCE GROUP ANALYSIS


experience_analysis = (
    individual_df
    .groupby("Experience_Group")
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

experience_analysis["Promoter_Percentage"] = (
    experience_analysis["Promoters"]
    / experience_analysis["Participants"]
) * 100

experience_analysis = experience_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "=" * 70)
print("EXPERIENCE GROUP ANALYSIS")
print("=" * 70)

print(experience_analysis)

experience_analysis.to_csv(
    TABLE_FOLDER / "experience_group_analysis.csv",
    index=False
)

print("Experience group analysis table saved.")

plt.figure(figsize=(10,5))

plt.bar(
    experience_analysis["Experience_Group"],
    experience_analysis["Average_NPS"]
)

plt.title("Average NPS by Experience Group")

plt.xlabel("Experience Group")

plt.ylabel("Average NPS")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "experience_group_analysis.png"
)

plt.close()

print("Experience group chart saved.")

# DESIGNATION ANALYSIS


designation_analysis = (
    individual_df
    .groupby("Designation")
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

designation_analysis["Promoter_Percentage"] = (
    designation_analysis["Promoters"]
    / designation_analysis["Participants"]
) * 100

designation_analysis = designation_analysis.sort_values(
    by="Average_NPS",
    ascending=False
)

print("\n" + "="*70)
print("DESIGNATION ANALYSIS")
print("="*70)

print(designation_analysis)

designation_analysis.to_csv(
    TABLE_FOLDER / "designation_analysis.csv",
    index=False
)

print("Designation analysis table saved.")

plt.figure(figsize=(12,6))

plt.bar(
    designation_analysis["Designation"],
    designation_analysis["Average_NPS"]
)

plt.title("Average NPS by Designation")

plt.xlabel("Designation")

plt.ylabel("Average NPS")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "designation_analysis.png"
)

plt.close()

print("Designation chart saved.")

# TOP & BOTTOM PERFORMERS

print("\n" + "="*70)
print("TOP & BOTTOM PERFORMING GROUPS")
print("="*70)

print("\nTop 5 Departments")
print(department_summary[["Dept","Average_NPS"]].head())

print("\nBottom 5 Departments")
print(department_summary[["Dept","Average_NPS"]].tail())

print("\nTop 5 Roles")
print(role_analysis[["Role","Average_NPS"]].head())

print("\nBottom 5 Roles")
print(role_analysis[["Role","Average_NPS"]].tail())

print("\nTop 5 Regions")
print(region_analysis[["Region","Average_NPS"]].head())

print("\nBottom 5 Regions")
print(region_analysis[["Region","Average_NPS"]].tail())

print("\nTop Age Group")
print(age_analysis[["Age_Group","Average_NPS"]].head(1))

print("\nLowest Age Group")
print(age_analysis[["Age_Group","Average_NPS"]].tail(1))

print("\nTop Experience Group")
print(experience_analysis[["Experience_Group","Average_NPS"]].head(1))

print("\nLowest Experience Group")
print(experience_analysis[["Experience_Group","Average_NPS"]].tail(1))


# INDIVIDUAL ANALYSIS REPORT


report_file = REPORT_FOLDER / "individual_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("="*70 + "\n")
    file.write("INDIVIDUAL NPS ANALYSIS REPORT\n")
    file.write("="*70 + "\n\n")

    file.write(f"Total Participants : {total_participants}\n")
    file.write(f"Average NPS : {average_nps:.2f}\n")
    file.write(f"Promoters : {promoters}\n")
    file.write(f"Passives : {passives}\n\n")

    file.write("TOP DEPARTMENT\n")
    file.write(str(department_summary.iloc[0]))
    file.write("\n\n")

    file.write("BOTTOM DEPARTMENT\n")
    file.write(str(department_summary.iloc[-1]))
    file.write("\n\n")

    file.write("TOP ROLE\n")
    file.write(str(role_analysis.iloc[0]))
    file.write("\n\n")

    file.write("TOP REGION\n")
    file.write(str(region_analysis.iloc[0]))
    file.write("\n\n")

    file.write("TOP AGE GROUP\n")
    file.write(str(age_analysis.iloc[0]))
    file.write("\n\n")

    file.write("TOP EXPERIENCE GROUP\n")
    file.write(str(experience_analysis.iloc[0]))
    file.write("\n\n")

print("Individual analysis report generated successfully.")