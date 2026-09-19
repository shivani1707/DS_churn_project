| Resource | URL |
|---|---|
| **GitHub Repository** | https://github.com/shivani1707/DS_churn_project|


# Telco Customer Churn Prediction

## 1. Project Overview

This project develops a machine learning solution to predict customer churn using the Telco Customer Churn dataset.

A Decision Tree Classifier is used to predict whether a customer is likely to churn.

The project includes:

* Data understanding and preprocessing
* Exploratory Data Analysis
* Feature engineering
* Decision Tree model development
* Comparison of two Decision Tree configurations
* Model evaluation
* Feature importance analysis
* Decision Tree visualization
* Saved machine learning pipeline
* FastAPI REST API for churn prediction

## 2. Project Structure

```text
customer_churn_project/
│
├── data/
│   └── TelcoCustomerChurn.csv
│
├── notebook/
│   └── churn_analysis.ipynb
│   └── telco_churn_model.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── sample_request.json
└── response_1789842843860.json

```

## 3. Machine Learning Model

Two Decision Tree configurations were evaluated:

### Model 1

* Criterion: Gini
* Maximum depth: 3
* Minimum samples per leaf: 8

### Model 2

* Criterion: Gini
* Maximum depth: 6
* Minimum samples per leaf: 8

The Depth 6 Decision Tree was selected as the final model because it achieved better Recall and F1 Score while maintaining reasonable Precision.

The complete preprocessing and model pipeline was saved as `churn_model.pkl`.

## 4. Installation

Python 3.10 or later is recommended.

Create or activate a Python environment if required.

Install the required packages:

```bash
pip install -r requirements.txt
```

Graphviz is also required to reproduce the Decision Tree visualization. It should be installed separately and available in the system PATH.

## 5. Running the API

Navigate to the project directory:

```bash
cd customer_churn_project
```

Start the FastAPI application:

```bash
python -m uvicorn app:app --reload --port 8001
```

The API will be available at:

```text
http://127.0.0.1:8001
```

## 6. API Documentation

FastAPI provides interactive API documentation at:

```text
http://127.0.0.1:8001/docs
```

The main prediction endpoint is:

```text
POST /predict
```

## 7. Prediction Request

The endpoint accepts customer information in JSON format.

Example:

```json
{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.50,
    "TotalCharges": 427.50
}
```

## 8. Prediction Response

Example response:

```json
{
    "prediction": "Yes",
    "churn_probability": 0.82
}
```

The `prediction` field indicates whether the customer is predicted to churn.

The `churn_probability` field represents the probability that the customer belongs to the churn class (`Yes`).

The probability shown above is an example and will depend on the input customer data and trained model.

## 9. Invalid Input Handling

The API uses Pydantic validation through FastAPI.

If required fields are missing or input values have an invalid data type, the API returns a validation error with HTTP status code `422`.

This prevents invalid customer data from being passed to the machine learning model.

## 10. Model Reusability

The saved `churn_model.pkl` contains the complete machine learning pipeline, including preprocessing and the trained Decision Tree model.

Therefore, new customer data can be passed directly to the pipeline without manually repeating the preprocessing steps.

## 11. Notebook

The complete data analysis and modelling process is available in:

```text
notebook/churn_analysis.ipynb
```

The notebook contains:

1. Data loading and understanding
2. Data cleaning
3. Exploratory Data Analysis
4. Feature engineering
5. Train/test split
6. Preprocessing
7. Decision Tree model development
8. Model comparison
9. Model evaluation
10. Feature importance
11. Decision Tree visualization
12. Model saving
