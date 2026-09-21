# NPS Analysis & Training Program Insights

## 📌 Project Overview

This project analyzes participant feedback from a training program to understand **Net Promoter Score (NPS), participant satisfaction, demographic patterns, and the factors associated with overall program experience**.

The analysis goes beyond calculating NPS by combining **data cleaning, exploratory data analysis, demographic analysis, feature engineering, composite indicators, predictive modeling, feature importance analysis, and root-cause analysis** to generate actionable insights for improving future training programs.

---

## 🎯 Objectives

The main objectives of this project are to:

* Calculate and analyze the **Net Promoter Score (NPS)**.
* Understand participant satisfaction and feedback patterns.
* Analyze responses across different demographic groups.
* Identify factors associated with participant experience.
* Create meaningful composite indicators from related survey questions.
* Apply predictive modeling to identify important factors influencing the outcome.
* Perform root-cause and gap analysis to identify areas requiring improvement.
* Translate analytical findings into actionable recommendations.

---

## 📊 Dataset

The dataset contains **161 cleaned participant responses** collected from a training program.

The survey contains information related to:

* Participant demographics
* Training experience
* Content quality
* Trainer effectiveness
* Learning environment
* Participant satisfaction
* NPS-related responses

The data was collected, cleaned and prepared before performing the analysis.

---

## 🧹 Data Preparation

The data preparation process included:

* Data inspection and profiling
* Handling missing and inconsistent values
* Data type standardization
* Duplicate checking
* Response validation
* Feature preparation
* Creation of analysis-ready datasets

The cleaned dataset was then used for exploratory analysis, statistical analysis, visualization, and modeling.

---

## 📈 NPS Analysis

Net Promoter Score was used as a primary measure of participant experience.

Participants were categorized based on their NPS responses, and the overall distribution was analyzed to understand the level of participant advocacy and satisfaction.

The project also examines NPS across relevant participant characteristics to identify patterns and differences between groups.

---

## 👥 Demographic Analysis

Participant demographics were analyzed to understand how the response population was distributed.

The analysis included factors such as:

* Age
* Gender
* Marital status
* Work experience
* Other available participant characteristics

These variables were compared with feedback and NPS-related outcomes to identify meaningful patterns.

---

## 🧩 Composite Indicators

Several related survey questions were grouped into broader analytical dimensions.

The project includes composite indicators representing areas such as:

* **Content Quality**
* **Trainer Effectiveness**
* **Learning Environment**
* **Overall Training Experience**

These indicators make it easier to evaluate broader aspects of the training program rather than analyzing every survey question independently.

---

## 🤖 Predictive Analysis

Predictive modeling was used to investigate which factors were associated with the target outcome.

The modeling workflow included:

1. Preparing the analytical dataset
2. Selecting relevant features
3. Preparing the target variable
4. Training predictive models
5. Evaluating model performance
6. Analyzing feature importance
7. Interpreting the results

The purpose of the modeling was **not to establish causation**, but to identify patterns and variables that were useful for predicting the outcome.

---

## 🔍 Root-Cause & Gap Analysis

The project also includes a structured analysis of gaps and potential improvement areas.

The analysis combines:

* Participant feedback
* Demographic patterns
* NPS-related results
* Composite indicators
* Predictive insights
* Feature importance

These findings were used to identify areas that could potentially contribute to lower participant satisfaction and require further attention.

---

## 💡 Key Insights

The analysis was designed to answer questions such as:

* What is the overall NPS of the training program?
* What proportion of participants fall into different NPS categories?
* How does participant experience vary across demographic groups?
* Which aspects of the training experience are most important?
* Which factors are most useful for predicting the target outcome?
* Where are the largest gaps in the participant experience?
* What areas should be prioritized for improvement?

Detailed findings and visualizations are available in the project's analysis outputs and reports.

---

## 📌 Recommendations

Based on the analytical findings, recommendations were developed around areas such as:

* Improving training content and delivery
* Strengthening trainer effectiveness
* Improving the learning environment
* Addressing identified participant-experience gaps
* Prioritizing areas with stronger relationships to the target outcome
* Using participant feedback to continuously improve future batches

The recommendations are based on the observed data patterns and is treated as **data-driven improvement suggestions rather than causal conclusions**.

---

## 🛠️ Technologies Used

### Programming & Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Development Environment

* Jupyter Notebook
* VS Code

### Data

* Excel
* CSV

---

## 🔄 Analysis Workflow

```text
Raw Survey Data
       ↓
Data Cleaning & Validation
       ↓
Exploratory Data Analysis
       ↓
NPS Analysis
       ↓
Demographic Analysis
       ↓
Feature Engineering
       ↓
Composite Indicators
       ↓
Predictive Modeling
       ↓
Feature Importance
       ↓
Root-Cause & Gap Analysis
       ↓
Actionable Recommendations
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Purni-r/nps-analysis.git
```

### 2. Navigate to the project

```bash
cd nps-analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the notebooks

Open the project in Jupyter Notebook or VS Code and execute the notebooks in the appropriate sequence.

---

## 📊 Project Outputs

The project produces analytical outputs including:

* NPS analysis
* Demographic analysis
* Participant distribution analysis
* Composite indicator analysis
* Predictive modeling results
* Feature importance analysis
* Root-cause analysis
* Gap analysis
* Visualizations
* Actionable recommendations

---

## ⚠️ Limitations

* The dataset contains **161 responses**, so findings should not automatically be generalized to larger populations.
* Survey responses represent participant perceptions and may contain subjective bias.
* Predictive relationships should not be interpreted as causal relationships.
* Additional batches and larger datasets would improve the reliability of future analysis.
* Future versions could incorporate longitudinal data to track changes in participant satisfaction over time.

---

## 👩‍💻 Author

**Purnima R**

* GitHub: [Purni-r](https://github.com/Purni-r)
* Mail: purnimaramesh03@gmail.com

---

## 📄 License

This project is intended for educational, analytical, and portfolio purposes.