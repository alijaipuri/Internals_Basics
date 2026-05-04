# Internals_Basics — MLOps CIE Submission

**USN:** 1BM23AI016
**Course:** MLOps (24AM6AEMLO)
**Date:** 04th May 2026
**Question Paper Code:** mlops-cie-013

## Scenario
CloudPulse is a cloud infrastructure provider. This project builds an MLOps pipeline to predict API response times to enforce SLA commitments and plan capacity.

## Dataset Features
| Feature | Range |
|---|---|
| request_size_kb | 1–500 |
| server_load | 0.1–1.0 |
| is_cached | 0–1 |
| region_latency | 10–200 |

**Target:** `response_time_ms` (milliseconds)

## Project Structure

Internals_Basics/
└── MLOPs_Lab_CIE/
    ├── data/
    │   └── training_data.csv
    ├── src/
    │   ├── train.py
    │   ├── tune.py
    │   ├── predict_cli.py
    │   └── api.py
    ├── models/
    │   └── best_model.pkl
    ├── results/
    │   ├── step1_s1.json
    │   ├── step2_s2.json
    │   ├── step3_s3.json
    │   └── step4_s4.json
    ├── requirements.txt
    ├── Dockerfile
    └── .gitignore

## Tasks

### Task 1 — Experiment Tracking & Model Comparison
- Trained Ridge and GradientBoosting models
- Logged MAE, RMSE, hyperparameters and tags to MLflow
- Experiment name: cloudpulse-response-time-ms
- Best model selected by lowest RMSE
- Result: results/step1_s1.json

### Task 2 — Hyperparameter Tuning
- Tuned best model using Grid Search with 5-fold cross-validation
- Parameter grid: n_estimators, learning_rate, max_depth
- Logged each trial as nested MLflow run under tuning-cloudpulse
- Result: results/step2_s2.json

### Task 3 — Docker Packaging
- Containerized CLI prediction tool
- Base image: python:3.12-slim
- Image: cloudpulse-predictor:v1
- Build: docker build -t cloudpulse-predictor:v1 .
- Run: docker run cloudpulse-predictor:v1 --request_size_kb 175.7 --server_load 0.4 --is_cached 0 --region_latency 132
- Result: results/step3_s3.json

### Task 4 — FastAPI Serving
- REST API serving best model on port 9000
- GET /ping — health check
- POST /score — prediction endpoint
- Pydantic validation with correct feature ranges
- Run: uvicorn src.api:app --port 9000
- Test: curl -X POST http://localhost:9000/score -H "Content-Type: application/json" -d '{"request_size_kb": 175.7, "server_load": 0.4, "is_cached": 0, "region_latency": 132}'
- Result: results/step4_s4.json

## Setup Instructions

Clone repo and enter folder:
git clone https://github.com/YOUR_USERNAME/Internals_Basics.git
cd Internals_Basics/MLOPs_Lab_CIE

Create and activate virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run Task 1:
python src/train.py

Run Task 2:
python src/tune.py

Run Task 4 API:
uvicorn src.api:app --port 9000

## Dependencies
- pandas
- numpy
- scikit-learn
- joblib
- mlflow
- fastapi
- uvicorn
- requests
