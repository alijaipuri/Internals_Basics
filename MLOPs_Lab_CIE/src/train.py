import pandas as pd
import numpy as np
import json
import os
import joblib
import mlflow
import mlflow.sklearn
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "training_data.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)
X = df[["request_size_kb", "server_load", "is_cached", "region_latency"]]
y = df["response_time_ms"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

EXPERIMENT_NAME = "cloudpulse-response-time-ms"
mlflow.set_experiment(EXPERIMENT_NAME)

models = {
    "Ridge": Ridge(alpha=1.0),
    "GradientBoosting": GradientBoostingRegressor(
        n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42
    ),
}

results = []

for model_name, model in models.items():
    with mlflow.start_run(run_name=model_name):
        mlflow.set_tag("priority", "high")

        # Log params
        params = model.get_params()
        mlflow.log_params(params)

        # Train
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))

        mlflow.log_metric("mae", mae)
        mlflow.log_metric("rmse", rmse)

        mlflow.sklearn.log_model(model, model_name)

        print(f"{model_name} → MAE: {mae:.4f}, RMSE: {rmse:.4f}")
        results.append({"name": model_name, "mae": round(mae, 4), "rmse": round(rmse, 4), "model": model})

# Select best by RMSE
best = min(results, key=lambda x: x["rmse"])
print(f"\nBest model: {best['name']} with RMSE={best['rmse']}")

# Save best model
joblib.dump(best["model"], os.path.join(MODELS_DIR, "best_model.pkl"))

# Save result JSON
output = {
    "experiment_name": EXPERIMENT_NAME,
    "models": [{"name": r["name"], "mae": r["mae"], "rmse": r["rmse"]} for r in results],
    "best_model": best["name"],
    "best_metric_name": "rmse",
    "best_metric_value": best["rmse"]
}

with open(os.path.join(RESULTS_DIR, "step1_s1.json"), "w") as f:
    json.dump(output, f, indent=2)

print("Saved results/step1_s1.json")
