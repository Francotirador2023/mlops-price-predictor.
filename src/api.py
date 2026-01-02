from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(title="House Price Predictor API")

# Load model
MODEL_PATH = "model.joblib"
if not os.path.exists(MODEL_PATH):
    # Fallback if running from a different directory context or if model not generated yet
    MODEL_PATH = "src/model.joblib"

try:
    model = joblib.load(MODEL_PATH)
except:
    model = None

class HousingFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def read_root():
    return {"status": "ok", "message": "House Price Predictor API is running"}

@app.post("/predict")
def predict_price(features: HousingFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    data_df = pd.DataFrame([features.dict()])
    prediction = model.predict(data_df)
    
    # Prediction is in 100k USD units
    price_value = prediction[0]
    
    return {
        "predicted_price_100k": price_value,
        "predicted_price_usd": price_value * 100000
    }
