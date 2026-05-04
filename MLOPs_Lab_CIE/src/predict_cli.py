import argparse
import joblib
import numpy as np
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_model.pkl")

parser = argparse.ArgumentParser()
parser.add_argument("--request_size_kb", type=float, required=True)
parser.add_argument("--server_load", type=float, required=True)
parser.add_argument("--is_cached", type=int, required=True)
parser.add_argument("--region_latency", type=float, required=True)
args = parser.parse_args()

model = joblib.load(MODEL_PATH)
features = np.array([[args.request_size_kb, args.server_load, args.is_cached, args.region_latency]])
prediction = float(model.predict(features)[0])

print(f"Predicted response_time_ms: {prediction:.4f}")
