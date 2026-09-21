# PURPOSE : Find factors affecting NPS

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
TABLE_FOLDER.mkdir(parents=True, exist_ok=True)

CHART_FOLDER = BASE_DIR / "outputs" / "charts"
CHART_FOLDER.mkdir(parents=True, exist_ok=True)

REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

individual_df = pd.read_csv(
    PROCESSED_FOLDER / "individual_featured.csv"
)

print("Dataset loaded successfully.")

# ==========================================================
# CORRELATION MATRIX
# ==========================================================

analysis_columns = [

    "NPS",

    "Job Relevance",

    "Content Clarity",

    "Learning Effectiveness",

    "Learner Engagement",

    "Trainer Facilitation",

    "Trainer Feedback Quality",

    "Learning Environment",

    "Overall Satisfaction",

    "Content_Quality_Index",

    "Trainer_Effectiveness_Index",

    "Learning_Environment_Index"

]

correlation_matrix = individual_df[
    analysis_columns
].corr()

print("\n" + "="*70)
print("CORRELATION MATRIX")
print("="*70)

print(correlation_matrix)

correlation_matrix.to_csv(
    TABLE_FOLDER / "correlation_matrix.csv"
)

print("Correlation matrix saved.")

# ==========================================================
# CORRELATION HEATMAP
# ==========================================================

plt.figure(figsize=(10,8))

plt.imshow(correlation_matrix, cmap="coolwarm", aspect="auto")

plt.colorbar()

plt.xticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation_matrix.columns)),
    correlation_matrix.columns
)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "correlation_heatmap.png"
)

plt.close()

print("Correlation heatmap saved.")

# ==========================================================
# ATTRIBUTE IMPORTANCE RANKING
# ==========================================================

attribute_importance = (
    correlation_matrix["NPS"]
    .drop("NPS")
    .abs()
    .sort_values(ascending=False)
    .reset_index()
)

attribute_importance.columns = [
    "Attribute",
    "Correlation_with_NPS"
]

print("\n" + "=" * 70)
print("ATTRIBUTE IMPORTANCE")
print("=" * 70)

print(attribute_importance)

attribute_importance.to_csv(
    TABLE_FOLDER / "attribute_importance.csv",
    index=False
)

plt.figure(figsize=(10,6))

plt.bar(
    attribute_importance["Attribute"],
    attribute_importance["Correlation_with_NPS"]
)

plt.xticks(rotation=75)

plt.ylabel("Correlation with NPS")

plt.title("Attribute Importance Ranking")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "attribute_importance.png"
)

plt.close()

print("Attribute importance chart saved.")

# ==========================================================
# TRAINER ATTRIBUTE ANALYSIS
# ==========================================================

trainer_attributes = [

    "Trainer Facilitation",

    "Trainer Feedback Quality"

]

trainer_analysis = individual_df[trainer_attributes].agg(
    ["mean", "std", "min", "max"]
).T

trainer_analysis.columns = [
    "Average",
    "Std_Deviation",
    "Minimum",
    "Maximum"
]

print("\n" + "=" * 70)
print("TRAINER ATTRIBUTE ANALYSIS")
print("=" * 70)

print(trainer_analysis)

trainer_analysis.to_csv(
    TABLE_FOLDER / "trainer_attribute_analysis.csv"
)

plt.figure(figsize=(6,5))

plt.bar(
    trainer_analysis.index,
    trainer_analysis["Average"]
)

plt.ylabel("Average Rating")

plt.title("Trainer Attribute Scores")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "trainer_attribute_analysis.png"
)

plt.close()

print("Trainer attribute chart saved.")

# ==========================================================
# LEARNING ATTRIBUTE ANALYSIS
# ==========================================================

learning_attributes = [

    "Job Relevance",

    "Content Clarity",

    "Learning Effectiveness",

    "Learner Engagement",

    "Learning Environment",

    "Overall Satisfaction"

]

learning_analysis = individual_df[learning_attributes].agg(
    ["mean", "std", "min", "max"]
).T

learning_analysis.columns = [

    "Average",

    "Std_Deviation",

    "Minimum",

    "Maximum"

]

print("\n" + "=" * 70)
print("LEARNING ATTRIBUTE ANALYSIS")
print("=" * 70)

print(learning_analysis)

learning_analysis.to_csv(
    TABLE_FOLDER / "learning_attribute_analysis.csv"
)

plt.figure(figsize=(8,5))

plt.bar(
    learning_analysis.index,
    learning_analysis["Average"]
)

plt.xticks(rotation=30)

plt.ylabel("Average Rating")

plt.title("Learning Attribute Scores")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "learning_attribute_analysis.png"
)

plt.close()

print("Learning attribute chart saved.")

# ==========================================================
# INSTRUCTOR IMPROVEMENT PRIORITY
# ==========================================================

instructor_priority = pd.DataFrame({

    "Attribute": [

        "Trainer Facilitation",

        "Trainer Feedback Quality",

        "Content Clarity",

        "Learning Effectiveness",

        "Learner Engagement",

        "Learning Environment",

        "Overall Satisfaction"

    ],

    "Average_Score": [

        individual_df["Trainer Facilitation"].mean(),

        individual_df["Trainer Feedback Quality"].mean(),

        individual_df["Content Clarity"].mean(),

        individual_df["Learning Effectiveness"].mean(),

        individual_df["Learner Engagement"].mean(),

        individual_df["Learning Environment"].mean(),

        individual_df["Overall Satisfaction"].mean()

    ],

    "Correlation_with_NPS": [

        correlation_matrix.loc["Trainer Facilitation", "NPS"],

        correlation_matrix.loc["Trainer Feedback Quality", "NPS"],

        correlation_matrix.loc["Content Clarity", "NPS"],

        correlation_matrix.loc["Learning Effectiveness", "NPS"],

        correlation_matrix.loc["Learner Engagement", "NPS"],

        correlation_matrix.loc["Learning Environment", "NPS"],

        correlation_matrix.loc["Overall Satisfaction", "NPS"]

    ]

})

instructor_priority["Priority_Score"] = (
    (4 - instructor_priority["Average_Score"])
    * instructor_priority["Correlation_with_NPS"]
)

instructor_priority = instructor_priority.sort_values(
    by="Priority_Score",
    ascending=False
)

print("\n" + "=" * 70)
print("INSTRUCTOR IMPROVEMENT PRIORITY")
print("=" * 70)

print(instructor_priority)

instructor_priority.to_csv(
    TABLE_FOLDER / "instructor_improvement_priority.csv",
    index=False
)

plt.figure(figsize=(10,6))

plt.bar(
    instructor_priority["Attribute"],
    instructor_priority["Priority_Score"]
)

plt.xticks(rotation=35)

plt.ylabel("Priority Score")

plt.title("Instructor Improvement Priority")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "instructor_improvement_priority.png"
)

plt.close()

print("Instructor improvement priority chart saved.")

# ==========================================================
# ATTRIBUTE IMPACT REPORT
# ==========================================================

report_file = REPORT_FOLDER / "attribute_impact_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 70 + "\n")
    file.write("ATTRIBUTE IMPACT ANALYSIS REPORT\n")
    file.write("=" * 70 + "\n\n")

    file.write("TOP ATTRIBUTES AFFECTING NPS\n")
    file.write("-" * 50 + "\n")
    file.write(
        attribute_importance
        .head(10)
        .to_string(index=False)
    )

    file.write("\n\n")

    file.write("TRAINER ATTRIBUTE SUMMARY\n")
    file.write("-" * 50 + "\n")
    file.write(
        trainer_analysis
        .to_string()
    )

    file.write("\n\n")

    file.write("LEARNING ATTRIBUTE SUMMARY\n")
    file.write("-" * 50 + "\n")
    file.write(
        learning_analysis
        .to_string()
    )

    file.write("\n\n")

    file.write("INSTRUCTOR IMPROVEMENT PRIORITY\n")
    file.write("-" * 50 + "\n")
    file.write(
        instructor_priority
        .to_string(index=False)
    )

print("\nAttribute impact report generated successfully.")
print(f"Report saved at : {report_file}")