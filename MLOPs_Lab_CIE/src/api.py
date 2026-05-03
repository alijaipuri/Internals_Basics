import pickle
import json
import os
from datetime import datetime
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# Load model
with open("models/best_model.pkl", "rb") as f:
    bundle = pickle.load(f)
MODEL = bundle["model"]
MODEL_NAME = bundle["name"]

app = FastAPI()

os.makedirs("logs", exist_ok=True)

class JobFeatures(BaseModel):
    gpu_memory_gb: float = Field(..., ge=8, le=80)
    batch_size: int = Field(..., ge=8, le=256)
    model_params_millions: float = Field(..., ge=10, le=7000)
    queue_depth: int = Field(..., ge=1, le=20)

@app.get("/status")
def status():
    return {"status": "running", "model": MODEL_NAME, "version": "1.0"}

@app.post("/estimate")
def estimate(job: JobFeatures):
    features = [[
        job.gpu_memory_gb,
        job.batch_size,
        job.model_params_millions,
        job.queue_depth
    ]]
    prediction = float(MODEL.predict(features)[0])
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": job.dict(),
        "prediction": round(prediction, 4),
        "endpoint": "/estimate"
    }
    with open("logs/predictions.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    return {"prediction": round(prediction, 4)}
