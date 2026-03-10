# EMI Prediction Application using Machine Learning

## Project Overview

This project focuses on building an intelligent system that predicts loan EMI amounts and EMI eligibility using machine learning techniques. Financial institutions and lending platforms often need quick and accurate EMI predictions to assist borrowers in understanding their repayment obligations.

The objective of this project is to develop machine learning models that can:
- Predict the monthly EMI amount for a loan applicant.
- Determine whether a user is eligible for EMI based on financial information.

The trained models are deployed through an interactive web application using **Streamlit**, allowing users to input their financial details and receive instant predictions.

---

## Objectives

| Objective | Description |
|---|---|
| **EMI Amount Prediction** | Develop a regression-based ML model that predicts monthly EMI values based on borrower information. |
| **EMI Eligibility Prediction** | Build a classification model to determine whether a borrower is eligible for EMI approval. |
| **Financial Decision Support** | Provide a tool that helps users estimate their financial commitments before applying for a loan. |
| **Real-Time Web Application** | Deploy the ML models using Streamlit for an interactive user interface. |

---

## Steps to Solve the Problem

### 1. Problem Identification
Loan applicants often need to estimate their EMI before applying for a loan. Traditional EMI calculations require manual formulas or financial calculators.

This project introduces a **machine learning-based EMI prediction system** that automates EMI calculation and eligibility assessment.

### 2. Data Collection
The dataset contains borrower financial and demographic attributes.

#### Dataset Features
| Feature | Feature |
|---|---|
| Gender | Monthly Salary |
| Marital Status | Years of Employment |
| Education | Monthly Rent |
| Employment Type | Family Size |
| Company Type | Other Monthly Expenses |
| House Type | Credit Score |
| Age | Current EMI Amount |
| Requested Loan Amount | Emergency Fund |
| Bank Balance | |

> These variables influence a person's ability to repay a loan.

### 3. Data Preprocessing

- **Handling Missing Values** – Missing values were identified and handled appropriately to maintain data quality.
- **Encoding Categorical Variables** – Features such as gender, education, and employment type were converted into numerical format using encoding techniques.
- **Feature Engineering** – Important financial attributes influencing EMI prediction were selected.
- **Feature Scaling** – Numerical variables were standardized to improve model performance.

### 4. Exploratory Data Analysis (EDA)

EDA was conducted to understand relationships between financial variables and EMI outcomes.

#### Key Insights
- Higher loan amounts increase EMI obligations.
- Credit score plays an important role in loan approval.
- Monthly salary influences EMI affordability.
- Existing loans affect EMI eligibility.
- Applicants with stronger financial stability show better EMI approval probability.

> Visualization techniques using **Matplotlib** and **Seaborn** were used to explore these relationships.

---

## Machine Learning Models Implemented

### Regression Model
- Used for **predicting the EMI Amount**
- Estimates the monthly EMI value based on financial and demographic attributes
- Saved as: `EMI Regression Model.pkl`

### Classification Model
- Used for **predicting EMI Eligibility**
- Determines whether a user is eligible for EMI approval
- Saved as: `EMI Classifier Model.pkl`

---

## Model Deployment

The trained models were deployed using **Streamlit**, allowing real-time predictions through a web interface. The application loads the trained models using `pickle` and performs predictions based on user inputs.

### Application Workflow
1. User enters financial and personal details.
2. Input data is converted into a structured dataframe.
3. The system uses the trained machine learning model.
4. Prediction results are displayed instantly.

### Streamlit Application Features

The application provides two prediction modes:

| Mode | Description |
|---|---|
| **EMI Amount Prediction** | Predicts the expected monthly EMI payment for a loan *(Regression streamlit file)* |
| **EMI Eligibility Prediction** | Determines whether the applicant is eligible for EMI approval *(Classification streamlit file)* |

The application interface allows users to enter:
- Salary
- Credit Score
- Requested Loan Amount
- Monthly Expenses
- Employment Details

---

## Technologies Used

| Category | Tools |
|---|---|
| **Programming Language** | Python |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Pickle |
| **Deployment Framework** | Streamlit |

---

## Project Files
```
 EMI-Prediction-ML
 ┣  notebook.ipynb               # Data analysis and model training
 ┣  dataset.csv                  # EMI prediction dataset
 ┣  EMI Regression Model.pkl     # Trained regression model
 ┣  EMI Classifier Model.pkl     # Trained classification model
 ┣  app_regression.py            # Streamlit regression app
 ┣  app_classification.py        # Streamlit classification app

```

---

## Results

The system successfully predicts:
-  Monthly EMI payment amount
-  EMI eligibility status

By integrating machine learning models with a Streamlit interface, the project provides a **practical and user-friendly financial prediction system**.

---

## Conclusion

This project demonstrates how machine learning can be applied to financial data to predict loan repayment obligations and borrower eligibility.

By combining **data preprocessing**, **machine learning models**, and **Streamlit deployment**, the system provides a real-time EMI prediction tool that helps users make informed financial decisions.

> Such applications can support **banks**, **fintech companies**, and **lending platforms** in improving loan evaluation processes and enhancing customer experience.
