# PURPOSE : Predictive Analysis using Machine Learning Models

import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_FOLDER = BASE_DIR / "data" / "processed"

REPORT_FOLDER = BASE_DIR / "outputs" / "reports"
TABLE_FOLDER = BASE_DIR / "outputs" / "tables"
CHART_FOLDER = BASE_DIR / "outputs" / "charts"
MODEL_FOLDER = BASE_DIR / "outputs" / "models"

REPORT_FOLDER.mkdir(parents=True, exist_ok=True)
TABLE_FOLDER.mkdir(parents=True, exist_ok=True)
CHART_FOLDER.mkdir(parents=True, exist_ok=True)
MODEL_FOLDER.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(PROCESSED_FOLDER / "individual_featured.csv")

print("Dataset loaded successfully.")

print("\n" + "=" * 70)
print("PREDICTIVE ANALYSIS")
print("=" * 70)

print(df.info())

print("\nFirst Five Records")
print(df.head())

# --------------------------------------------------
# DATA PREPARATION
# --------------------------------------------------

print("\n" + "=" * 70)
print("DATA PREPARATION")
print("=" * 70)

# Target Variable
target_column = "NPS"

# Engineered Features for Prediction
required_features = [
    "Age_Years",
    "Experience_Years",
    "Content_Quality_Index",
    "Trainer_Effectiveness_Index",
    "Learning_Environment_Index"
]

# Verify all required features exist
missing_features = [
    feature for feature in required_features
    if feature not in df.columns
]

if missing_features:
    raise ValueError(
        f"Missing feature(s) in dataset: {missing_features}"
    )

# Prepare Feature Matrix and Target Variable
X = df[required_features]

y = df[target_column]

print(f"Target Variable : {target_column}")

print("\nSelected Features")
for feature in required_features:
    print(f"• {feature}")

print(f"\nTotal Features Used : {X.shape[1]}")
print(f"Total Records       : {len(df)}")

# --------------------------------------------------
# TRAIN - TEST SPLIT
# --------------------------------------------------

from sklearn.model_selection import train_test_split

print("\n" + "=" * 70)
print("TRAIN - TEST SPLIT")
print("=" * 70)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

print("\nTraining Feature Shape")
print(X_train.shape)

print("\nTesting Feature Shape")
print(X_test.shape)

print("\nTraining Target Shape")
print(y_train.shape)

print("\nTesting Target Shape")
print(y_test.shape)

# --------------------------------------------------
# TRAIN MULTIPLE MODELS
# --------------------------------------------------

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

print("\n" + "=" * 70)
print("TRAIN MULTIPLE MODELS")
print("=" * 70)

# Dictionary to store trained models
trained_models = {}

# --------------------------------------------------
# Linear Regression
# --------------------------------------------------

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

trained_models["Linear Regression"] = linear_model

print("✓ Linear Regression trained successfully.")

# --------------------------------------------------
# Decision Tree Regressor
# --------------------------------------------------

decision_tree_model = DecisionTreeRegressor(
    random_state=42
)

decision_tree_model.fit(X_train, y_train)

trained_models["Decision Tree"] = decision_tree_model

print("✓ Decision Tree Regressor trained successfully.")

# --------------------------------------------------
# Random Forest Regressor
# --------------------------------------------------

random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

random_forest_model.fit(X_train, y_train)

trained_models["Random Forest"] = random_forest_model

print("✓ Random Forest Regressor trained successfully.")

# --------------------------------------------------
# Training Summary
# --------------------------------------------------

print("\n" + "=" * 70)
print("TRAINING SUMMARY")
print("=" * 70)

print(f"Total Models Trained : {len(trained_models)}")

print("\nModels")

for model_name in trained_models.keys():
    print(f"• {model_name}")



# --------------------------------------------------
# MODEL EVALUATION
# --------------------------------------------------

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np

print("\n" + "=" * 70)
print("MODEL EVALUATION")
print("=" * 70)

# Store evaluation results
evaluation_results = []

# Store predictions
model_predictions = {}

for model_name, model in trained_models.items():

    # Predict on Test Data
    predictions = model.predict(X_test)

    model_predictions[model_name] = predictions

    # Calculate Metrics
    mae = mean_absolute_error(y_test, predictions)

    rmse = np.sqrt(
        mean_squared_error(y_test, predictions)
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    evaluation_results.append({
        "Model": model_name,
        "MAE": round(mae, 4),
        "RMSE": round(rmse, 4),
        "R2_Score": round(r2, 4)
    })

# Create Evaluation Table
evaluation_df = pd.DataFrame(evaluation_results)

# Sort by Best R² Score
evaluation_df = evaluation_df.sort_values(
    by="R2_Score",
    ascending=False
).reset_index(drop=True)

print(evaluation_df)

# Save Evaluation Table
evaluation_df.to_csv(
    TABLE_FOLDER / "model_comparison.csv",
    index=False
)

print("\nModel comparison table saved.")

# --------------------------------------------------
# BEST MODEL SELECTION
# --------------------------------------------------

print("\n" + "=" * 70)
print("BEST MODEL SELECTION")
print("=" * 70)

# Sort by Highest R² and Lowest RMSE
evaluation_df = evaluation_df.sort_values(
    by=["R2_Score", "RMSE"],
    ascending=[False, True]
).reset_index(drop=True)

# Best Model Name
best_model_name = evaluation_df.loc[0, "Model"]

# Best Model Object
best_model = trained_models[best_model_name]

# Best Model Predictions
best_predictions = model_predictions[best_model_name]

print(f"Best Model : {best_model_name}")

print("\nPerformance")

print(f"MAE       : {evaluation_df.loc[0, 'MAE']:.4f}")
print(f"RMSE      : {evaluation_df.loc[0, 'RMSE']:.4f}")
print(f"R² Score  : {evaluation_df.loc[0, 'R2_Score']:.4f}")

# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("\n" + "=" * 70)
print("FEATURE IMPORTANCE")
print("=" * 70)

# Get Feature Importance Automatically
if hasattr(best_model, "feature_importances_"):

    importance = best_model.feature_importances_

elif hasattr(best_model, "coef_"):

    importance = np.abs(best_model.coef_)

else:

    raise ValueError(
        "Selected model does not support feature importance."
    )

# Create Feature Importance Table
feature_importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance": importance

})

feature_importance_df = feature_importance_df.sort_values(

    by="Importance",

    ascending=False

).reset_index(drop=True)

print(feature_importance_df)

# Save Table
feature_importance_df.to_csv(

    TABLE_FOLDER / "predictive_feature_importance.csv",

    index=False

)

print("Predictive feature importance table saved.")

# --------------------------------------------------
# Feature Importance Chart
# --------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(

    feature_importance_df["Feature"],

    feature_importance_df["Importance"]

)

plt.title(f"Feature Importance ({best_model_name})")

plt.xlabel("Features")

plt.ylabel("Importance")

plt.xticks(rotation=30, ha="right")

plt.tight_layout()

plt.savefig(

    CHART_FOLDER / "predictive_feature_importance.png",

    dpi=300

)

plt.close()

print("Predictive feature importance chart saved.")

# --------------------------------------------------
# ACTUAL VS PREDICTED
# --------------------------------------------------

print("\n" + "=" * 70)
print("ACTUAL VS PREDICTED")
print("=" * 70)

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    best_predictions,
    alpha=0.7
)

# Perfect Prediction Line
minimum = min(y_test.min(), best_predictions.min())
maximum = max(y_test.max(), best_predictions.max())

plt.plot(
    [minimum, maximum],
    [minimum, maximum],
    linestyle="--"
)

plt.title(f"Actual vs Predicted NPS ({best_model_name})")

plt.xlabel("Actual NPS")

plt.ylabel("Predicted NPS")

plt.tight_layout()

plt.savefig(
    CHART_FOLDER / "actual_vs_predicted.png",
    dpi=300
)

plt.close()

print("Actual vs Predicted chart saved.")


# --------------------------------------------------
# SAVE BEST MODEL
# --------------------------------------------------

import joblib

print("\n" + "=" * 70)
print("SAVE BEST MODEL")
print("=" * 70)

# Save Best Model
model_file = MODEL_FOLDER / "best_nps_model.pkl"

joblib.dump(
    best_model,
    model_file
)

print(f"Best model ({best_model_name}) saved successfully.")
print(f"Model saved at : {model_file}")


# --------------------------------------------------
# PREDICTIVE ANALYSIS REPORT
# --------------------------------------------------

print("\n" + "=" * 70)
print("PREDICTIVE ANALYSIS REPORT")
print("=" * 70)

report_file = REPORT_FOLDER / "predictive_analysis_report.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("=" * 70 + "\n")
    file.write("PREDICTIVE ANALYSIS REPORT\n")
    file.write("=" * 70 + "\n\n")

    file.write("Dataset Information\n")
    file.write("-" * 35 + "\n")
    file.write(f"Total Records           : {len(df)}\n")
    file.write(f"Training Records        : {len(X_train)}\n")
    file.write(f"Testing Records         : {len(X_test)}\n\n")

    file.write("Target Variable\n")
    file.write("-" * 35 + "\n")
    file.write(f"{target_column}\n\n")

    file.write("Features Used\n")
    file.write("-" * 35 + "\n")

    for feature in required_features:
        file.write(f"• {feature}\n")

    file.write("\n")

    file.write("Models Trained\n")
    file.write("-" * 35 + "\n")

    for model in trained_models.keys():
        file.write(f"• {model}\n")

    file.write("\n")

    file.write("Model Performance\n")
    file.write("-" * 35 + "\n")
    file.write(
        evaluation_df.to_string(index=False)
    )

    file.write("\n\n")

    file.write("Best Model\n")
    file.write("-" * 35 + "\n")
    file.write(f"Model      : {best_model_name}\n")
    file.write(f"MAE        : {evaluation_df.loc[0,'MAE']:.4f}\n")
    file.write(f"RMSE       : {evaluation_df.loc[0,'RMSE']:.4f}\n")
    file.write(f"R² Score   : {evaluation_df.loc[0,'R2_Score']:.4f}\n\n")

    file.write("Top Predictive Features\n")
    file.write("-" * 35 + "\n")

    for _, row in feature_importance_df.iterrows():
        file.write(
            f"{row['Feature']} : {row['Importance']:.4f}\n"
        )

print("Predictive analysis report generated successfully.")
print(f"Report saved at : {report_file}")