import joblib

from fastapi import FastAPI
from pydantic import BaseModel


# Create FastAPI application
app = FastAPI(
    title="Telco Customer Churn Prediction API",
    description="API for predicting customer churn",
    version="1.0.0"
)


# Load the trained pipeline
model = joblib.load("notebook/telco_churn_model.pkl")


# Define the expected customer input
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {
        "message": "Telco Customer Churn Prediction API is running"
    }


@app.post("/predict")
def predict(customer: CustomerData):

    # Convert JSON input to DataFrame
    customer_data = customer.model_dump()

    import pandas as pd

    input_df = pd.DataFrame([customer_data])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Get probability of churn
    probabilities = model.predict_proba(input_df)[0]

    # Find the probability corresponding to "Yes"
    classes = model.classes_

    yes_index = list(classes).index("Yes")

    churn_probability = probabilities[yes_index]

    return {
        "prediction": prediction,
        "churn_probability": round(float(churn_probability), 4)
    }