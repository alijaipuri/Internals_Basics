from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

app = FastAPI()
model = joblib.load(MODEL_PATH)

class Features(BaseModel):
    request_size_kb: float = Field(..., ge=1, le=500)
    server_load: float = Field(..., ge=0.1, le=1.0)
    is_cached: int = Field(..., ge=0, le=1)
    region_latency: float = Field(..., ge=10, le=200)

@app.get("/ping")
def ping():
    return {"status": "healthy", "model_loaded": True}

@app.post("/score")
def score(features: Features):
    X = np.array([[
        features.request_size_kb,
        features.server_load,
        features.is_cached,
        features.region_latency
    ]])
    prediction = float(model.predict(X)[0])
    return {"prediction": prediction}
