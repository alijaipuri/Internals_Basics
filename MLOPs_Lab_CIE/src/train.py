import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import json
import os
import pickle
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load data
df = pd.read_csv("data/training_data.csv")
X = df[["gpu_memory_gb", "batch_size", "model_params_millions", "queue_depth"]]
y = df["job_completion_min"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

def compute_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return {"mae": round(mae, 4), "rmse": round(rmse, 4),
            "r2": round(r2, 4), "mape": round(mape, 4)}

mlflow.set_experiment("gpuforge-job-completion")

results = []
trained_models = {}

# --- Ridge ---
with mlflow.start_run(run_name="Ridge"):
    mlflow.set_tag("experiment_type", "baseline_comparison")
    params = {"alpha": 1.0, "fit_intercept": True}
    model = Ridge(**params)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    metrics = compute_metrics(y_test.values, preds)
    mlflow.log_params(params)
    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(model, "ridge_model")
    results.append({"name": "Ridge", **metrics})
    trained_models["Ridge"] = model
    print(f"Ridge -> {metrics}")

# --- GradientBoosting ---
with mlflow.start_run(run_name="GradientBoosting"):
    mlflow.set_tag("experiment_type", "baseline_comparison")
    params = {"n_estimators": 100, "learning_rate": 0.1,
              "max_depth": 3, "random_state": 42}
    model = GradientBoostingRegressor(**params)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    metrics = compute_metrics(y_test.values, preds)
    mlflow.log_params(params)
    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(model, "gb_model")
    results.append({"name": "GradientBoosting", **metrics})
    trained_models["GradientBoosting"] = model
    print(f"GradientBoosting -> {metrics}")

# Pick best by RMSE
best = min(results, key=lambda x: x["rmse"])

# Save best model to disk
os.makedirs("models", exist_ok=True)
with open("models/best_model.pkl", "wb") as f:
    pickle.dump({"model": trained_models[best["name"]], "name": best["name"]}, f)
print(f"\nBest model: {best['name']} saved to models/best_model.pkl")

# Print result JSON
output = {
    "experiment_name": "gpuforge-job-completion",
    "models": results,
    "best_model": best["name"],
    "best_metric_name": "rmse",
    "best_metric_value": best["rmse"]
}
print("\n===== TASK 1 RESULT =====")
print(json.dumps(output, indent=2))
