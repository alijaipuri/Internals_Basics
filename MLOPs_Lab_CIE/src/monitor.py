import json
import pandas as pd
import numpy as np

# Load training data
train_df = pd.read_csv("data/training_data.csv")
train_model_params_mean = train_df["model_params_millions"].mean()
train_queue_depth_mean = train_df["queue_depth"].mean()

# Load live predictions
live_entries = []
with open("logs/predictions.jsonl") as f:
    for line in f:
        live_entries.append(json.loads(line.strip()))

total = len(live_entries)
predictions = [e["prediction"] for e in live_entries]
mean_prediction = round(np.mean(predictions), 4)

live_model_params = [e["input"]["model_params_millions"] for e in live_entries]
live_queue_depth = [e["input"]["queue_depth"] for e in live_entries]

live_model_params_mean = round(np.mean(live_model_params), 4)
live_queue_depth_mean = round(np.mean(live_queue_depth), 4)

shift_mp = round(abs(live_model_params_mean - train_model_params_mean), 4)
shift_qd = round(abs(live_queue_depth_mean - train_queue_depth_mean), 4)

status_mp = "ALERT" if shift_mp > 500 else "OK"
status_qd = "ALERT" if shift_qd > 5 else "OK"
drift_detected = status_mp == "ALERT" or status_qd == "ALERT"

print(f"model_params_millions — train_mean={round(train_model_params_mean,4)}, "
      f"live_mean={live_model_params_mean}, shift={shift_mp}, threshold=500 → {status_mp}")
print(f"queue_depth           — train_mean={round(train_queue_depth_mean,4)}, "
      f"live_mean={live_queue_depth_mean}, shift={shift_qd}, threshold=5 → {status_qd}")
print(f"Drift detected: {drift_detected}")

output = {
    "total_predictions": total,
    "mean_prediction": mean_prediction,
    "drift_detected": drift_detected,
    "alerts": [
        {
            "feature": "model_params_millions",
            "train_mean": round(train_model_params_mean, 4),
            "live_mean": live_model_params_mean,
            "shift": shift_mp,
            "threshold": 500,
            "status": status_mp
        },
        {
            "feature": "queue_depth",
            "train_mean": round(train_queue_depth_mean, 4),
            "live_mean": live_queue_depth_mean,
            "shift": shift_qd,
            "threshold": 5,
            "status": status_qd
        }
    ]
}

print("\n===== TASK 3 RESULT =====")
print(json.dumps(output, indent=2))
