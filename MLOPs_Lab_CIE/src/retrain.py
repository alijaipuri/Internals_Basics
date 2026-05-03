import pandas as pd
import numpy as np
import pickle
import json
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load champion info
with open("models/best_model.pkl", "rb") as f:
    bundle = pickle.load(f)
champion_model = bundle["model"]
champion_name = bundle["name"]

# Original test set (same split as Task 1)
train_df = pd.read_csv("data/training_data.csv")
X_orig = train_df[["gpu_memory_gb", "batch_size", "model_params_millions", "queue_depth"]]
y_orig = train_df["job_completion_min"]
X_train_orig, X_test, y_train_orig, y_test = train_test_split(
    X_orig, y_orig, test_size=0.2, random_state=42
)

# Champion RMSE on same test set
champ_preds = champion_model.predict(X_test)
champion_rmse = round(np.sqrt(mean_squared_error(y_test, champ_preds)), 4)

# Load new data
new_df = pd.read_csv("data/new_data.csv")
combined_df = pd.concat([train_df, new_df], ignore_index=True)

X_combined = combined_df[["gpu_memory_gb", "batch_size", "model_params_millions", "queue_depth"]]
y_combined = combined_df["job_completion_min"]
X_train_new, _, y_train_new, _ = train_test_split(
    X_combined, y_combined, test_size=0.2, random_state=42
)

# Retrain same model type
if champion_name == "Ridge":
    retrained = Ridge(alpha=1.0, fit_intercept=True)
else:
    retrained = GradientBoostingRegressor(
        n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42
    )

retrained.fit(X_train_new, y_train_new)
retrained_preds = retrained.predict(X_test)
retrained_rmse = round(np.sqrt(mean_squared_error(y_test, retrained_preds)), 4)

improvement = round(champion_rmse - retrained_rmse, 4)
action = "promoted" if improvement >= 0.5 else "kept_champion"

if action == "promoted":
    with open("models/best_model.pkl", "wb") as f:
        pickle.dump({"model": retrained, "name": champion_name}, f)
    print("Retrained model PROMOTED and saved.")
else:
    print("Champion retained — improvement below threshold.")

output = {
    "original_data_rows": len(train_df),
    "new_data_rows": len(new_df),
    "combined_data_rows": len(combined_df),
    "champion_rmse": champion_rmse,
    "retrained_rmse": retrained_rmse,
    "improvement": improvement,
    "min_improvement_threshold": 0.5,
    "action": action,
    "comparison_metric": "rmse"
}

print("\n===== TASK 4 RESULT =====")
print(json.dumps(output, indent=2))
