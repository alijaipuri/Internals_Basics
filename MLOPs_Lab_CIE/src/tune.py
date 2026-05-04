import pandas as pd
import numpy as np
import json
import os
import joblib
import mlflow
import mlflow.sklearn
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, make_scorer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "training_data.csv")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(RESULTS_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)
X = df[["request_size_kb", "server_load", "is_cached", "region_latency"]]
y = df["response_time_ms"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

param_grid = {
    "n_estimators": [50, 100, 200],
    "learning_rate": [0.05, 0.1, 0.2],
    "max_depth": [3, 5],
}

PARENT_RUN_NAME = "tuning-cloudpulse"
mlflow.set_experiment("cloudpulse-response-time-ms")

rmse_scorer = make_scorer(
    lambda y_true, y_pred: np.sqrt(mean_squared_error(y_true, y_pred)),
    greater_is_better=False
)

with mlflow.start_run(run_name=PARENT_RUN_NAME) as parent_run:
    total_trials = 0

    all_trials = []

    for n_est in param_grid["n_estimators"]:
        for lr in param_grid["learning_rate"]:
            for md in param_grid["max_depth"]:
                params = {"n_estimators": n_est, "learning_rate": lr, "max_depth": md}
                model = GradientBoostingRegressor(random_state=42, **params)

                cv_scores = cross_val_score(
                    model, X_train, y_train,
                    cv=5,
                    scoring=make_scorer(mean_absolute_error, greater_is_better=False)
                )
                cv_mae = -cv_scores.mean()

                model.fit(X_train, y_train)
                preds = model.predict(X_test)
                mae = mean_absolute_error(y_test, preds)
                rmse = np.sqrt(mean_squared_error(y_test, preds))

                with mlflow.start_run(run_name=f"trial_{total_trials+1}", nested=True):
                    mlflow.log_params(params)
                    mlflow.log_metric("mae", mae)
                    mlflow.log_metric("rmse", rmse)
                    mlflow.log_metric("cv_mae", cv_mae)

                all_trials.append({
                    "params": params,
                    "mae": mae,
                    "rmse": rmse,
                    "cv_mae": cv_mae,
                    "model": model
                })
                total_trials += 1

    best = min(all_trials, key=lambda x: x["rmse"])
    print(f"Best params: {best['params']}, RMSE: {best['rmse']:.4f}")

    # Save best tuned model (overwrite)
    joblib.dump(best["model"], os.path.join(MODELS_DIR, "best_model.pkl"))

    output = {
        "search_type": "grid",
        "n_folds": 5,
        "total_trials": total_trials,
        "best_params": best["params"],
        "best_mae": round(best["mae"], 4),
        "best_cv_mae": round(best["cv_mae"], 4),
        "parent_run_name": PARENT_RUN_NAME
    }

    with open(os.path.join(RESULTS_DIR, "step2_s2.json"), "w") as f:
        json.dump(output, f, indent=2)

print(f"Total trials: {total_trials}")
print("Saved results/step2_s2.json")
