import requests
import random
import json

BASE = "http://localhost:8500"

# 40 normal requests (within training data ranges)
normal_inputs = []
for _ in range(40):
    normal_inputs.append({
        "gpu_memory_gb": random.choice([8, 16, 24, 32, 40, 48, 56, 64, 72, 80]),
        "batch_size": random.choice([8, 16, 32, 64, 128, 256]),
        "model_params_millions": round(random.uniform(10, 1000), 1),
        "queue_depth": random.randint(1, 10)
    })

# 10 drifted requests (new_data.csv ranges — large models, deep queues)
drifted_inputs = []
for _ in range(10):
    drifted_inputs.append({
        "gpu_memory_gb": random.choice([64, 72, 80]),
        "batch_size": random.choice([128, 256]),
        "model_params_millions": round(random.uniform(4000, 7000), 1),
        "queue_depth": random.randint(14, 20)
    })

all_inputs = normal_inputs + drifted_inputs
print(f"Sending {len(all_inputs)} requests...")

for i, inp in enumerate(all_inputs):
    r = requests.post(f"{BASE}/estimate", json=inp)
    if r.status_code == 200:
        print(f"[{i+1}/50] prediction={r.json()['prediction']}")
    else:
        print(f"[{i+1}/50] ERROR {r.status_code}: {r.text}")

print("\nDone. Check logs/predictions.jsonl")
