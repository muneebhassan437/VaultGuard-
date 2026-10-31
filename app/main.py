from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd
from validation import TransactionInput

app = FastAPI()
model = joblib.load("../models/logistic_regression_model.joblib")  # Load your pre-trained model here

@app.get("/")
def read_root():
    return {"message": "Welcome to the VaultGuard AI API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(input_data: TransactionInput):
    # Convert the input data to a dictionary and then to a DataFrame
    input_dict = input_data.model_dump()  # Use model_dump() to get a dictionary representation of the Pydantic model
    input_df = pd.DataFrame([input_dict])
    
    # Make prediction using the pre-trained model
    prediction = model.predict(input_df)
    
    # Return the prediction result
    return {"is_fraud": bool(prediction[0])}
