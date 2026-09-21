# PURPOSE: Prepare datasets for dashboard integration

import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
CHART_FOLDER = BASE_DIR / "outputs" / "charts"
REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
DASHBOARD_FOLDER = BASE_DIR / "outputs" / "dashboard"

TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)
DASHBOARD_FOLDER.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Project Outputs
# --------------------------------------------------

# Main Dataset
df = pd.read_csv(
    PROCESSED_FOLDER / "individual_featured.csv"
)

# Batch Dataset
batch_df = pd.read_csv(
    PROCESSED_FOLDER / "batch_cleaned.csv"
)

print("Project datasets loaded successfully.")

print("\n" + "=" * 70)
print("DASHBOARD & PROJECT INTEGRATION")
print("=" * 70)

print("\nIndividual Dataset Information")
print(df.info())

print("\nFirst Five Records")
print(df.head())

print("\nBatch Dataset Information")
print(batch_df.info())

print("\nFirst Five Records")
print(batch_df.head())

# --------------------------------------------------
# DASHBOARD SUMMARY DATASET
# --------------------------------------------------

print("\n" + "=" * 70)
print("DASHBOARD SUMMARY DATASET")
print("=" * 70)

participants = len(df)

promoters = (df["NPS_Category"] == "Promoter").sum()

passives = (df["NPS_Category"] == "Passive").sum()

detractors = (df["NPS_Category"] == "Detractor").sum()

dashboard_summary = pd.DataFrame({
    "Metric": [
        "Total Participants",
        "Average NPS",
        "Promoters",
        "Passives",
        "Detractors",
        "Promoter Percentage",
        "Average Content Index",
        "Average Trainer Index",
        "Average Environment Index"
    ],
    "Value": [
        participants,
        round(df["NPS"].mean(), 2),
        promoters,
        passives,
        detractors,
        round((promoters / participants) * 100, 2),
        round(df["Content_Quality_Index"].mean(), 2),
        round(df["Trainer_Effectiveness_Index"].mean(), 2),
        round(df["Learning_Environment_Index"].mean(), 2)
    ]
})

print(dashboard_summary)

dashboard_summary.to_csv(
    DASHBOARD_FOLDER / "dashboard_summary.csv",
    index=False
)

print("Dashboard summary dataset saved.")

# --------------------------------------------------
# DASHBOARD KPI DATASET
# --------------------------------------------------

print("\n" + "=" * 70)
print("DASHBOARD KPI DATASET")
print("=" * 70)

kpi_df = pd.DataFrame({
    "KPI": [
        "Overall NPS",
        "Total Participants",
        "Promoters",
        "Passives",
        "Detractors",
        "Promoter Percentage",
        "Average Content Quality",
        "Average Trainer Effectiveness",
        "Average Learning Environment"
    ],
    "Value": [
        round(df["NPS"].mean(), 2),
        len(df),
        (df["NPS_Category"] == "Promoter").sum(),
        (df["NPS_Category"] == "Passive").sum(),
        (df["NPS_Category"] == "Detractor").sum(),
        round(
            (df["NPS_Category"] == "Promoter").mean() * 100,
            2
        ),
        round(df["Content_Quality_Index"].mean(), 2),
        round(df["Trainer_Effectiveness_Index"].mean(), 2),
        round(df["Learning_Environment_Index"].mean(), 2)
    ]
})

print(kpi_df)

kpi_df.to_csv(
    DASHBOARD_FOLDER / "dashboard_kpi.csv",
    index=False
)

print("Dashboard KPI dataset saved.")

# --------------------------------------------------
# DASHBOARD CHART INDEX
# --------------------------------------------------

print("\n" + "=" * 70)
print("DASHBOARD CHART INDEX")
print("=" * 70)

# Get all PNG chart files
chart_files = sorted(CHART_FOLDER.glob("*.png"))

chart_index = pd.DataFrame({
    "Chart_Name": [chart.stem for chart in chart_files],
    "File_Name": [chart.name for chart in chart_files],
    "File_Path": [str(chart) for chart in chart_files]
})

print(chart_index)

chart_index.to_csv(
    DASHBOARD_FOLDER / "dashboard_chart_index.csv",
    index=False
)

print(f"Total Charts : {len(chart_index)}")
print("Dashboard chart index saved.")

# --------------------------------------------------
# DASHBOARD TABLE INDEX
# --------------------------------------------------

print("\n" + "=" * 70)
print("DASHBOARD TABLE INDEX")
print("=" * 70)

# Get all CSV table files
table_files = sorted(TABLE_FOLDER.glob("*.csv"))

table_index = pd.DataFrame({
    "Table_Name": [table.stem for table in table_files],
    "File_Name": [table.name for table in table_files],
    "File_Path": [str(table) for table in table_files]
})

print(table_index)

table_index.to_csv(
    DASHBOARD_FOLDER / "dashboard_table_index.csv",
    index=False
)

print(f"Total Tables : {len(table_index)}")
print("Dashboard table index saved.")

# --------------------------------------------------
# DASHBOARD METADATA
# --------------------------------------------------

print("\n" + "=" * 70)
print("DASHBOARD METADATA")
print("=" * 70)

from datetime import datetime

metadata = pd.DataFrame({
    "Property": [
        "Project Name",
        "Generated On",
        "Total Participants",
        "Total Charts",
        "Total Tables",
        "Total Reports",
        "Total Dashboard Files",
        "Best Model"
    ],
    "Value": [
        "NPS Analytics Project",
        datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        len(df),
        len(list(CHART_FOLDER.glob("*.png"))),
        len(list(TABLE_FOLDER.glob("*.csv"))),
        len(list(REPORT_FOLDER.glob("*.txt"))),
        len(list(DASHBOARD_FOLDER.glob("*.csv"))),
        "best_nps_model.pkl"
    ]
})

print(metadata)

metadata.to_csv(
    DASHBOARD_FOLDER / "dashboard_metadata.csv",
    index=False
)

print("Dashboard metadata saved.")

# --------------------------------------------------
# DASHBOARD INTEGRATION REPORT
# --------------------------------------------------

print("\n" + "=" * 70)
print("DASHBOARD INTEGRATION REPORT")
print("=" * 70)

report_file = REPORT_FOLDER / "dashboard_integration_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 70 + "\n")
    file.write("DASHBOARD INTEGRATION REPORT\n")
    file.write("=" * 70 + "\n\n")

    file.write("Project Summary\n")
    file.write("-" * 35 + "\n")
    file.write(f"Total Participants : {len(df)}\n")
    file.write(f"Average NPS        : {df['NPS'].mean():.2f}\n")
    file.write(f"Promoters          : {(df['NPS_Category'] == 'Promoter').sum()}\n")
    file.write(f"Passives           : {(df['NPS_Category'] == 'Passive').sum()}\n")
    file.write(f"Detractors         : {(df['NPS_Category'] == 'Detractor').sum()}\n\n")

    file.write("Project Outputs\n")
    file.write("-" * 35 + "\n")
    file.write(f"Charts Generated        : {len(list(CHART_FOLDER.glob('*.png')))}\n")
    file.write(f"Tables Generated        : {len(list(TABLE_FOLDER.glob('*.csv')))}\n")
    file.write(f"Reports Generated       : {len(list(REPORT_FOLDER.glob('*.txt')))}\n")
    file.write(f"Dashboard Files Created : {len(list(DASHBOARD_FOLDER.glob('*.csv')))}\n\n")

    file.write("Dashboard Files\n")
    file.write("-" * 35 + "\n")

    for dashboard_file in sorted(DASHBOARD_FOLDER.glob("*.csv")):
        file.write(f"{dashboard_file.name}\n")

    file.write("\n")

    file.write("Available Reports\n")
    file.write("-" * 35 + "\n")

    for report in sorted(REPORT_FOLDER.glob("*.txt")):
        file.write(f"{report.name}\n")

    file.write("\n")

    file.write("Model Information\n")
    file.write("-" * 35 + "\n")
    file.write("Best Model : best_nps_model.pkl\n\n")

    file.write("Dashboard Integration Completed Successfully.\n")

print("Dashboard integration report generated successfully.")
print(f"Report saved at : {report_file}")