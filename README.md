<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=00D4FF&center=true&vCenter=true&width=600&lines=CloudPulse+Response+Predictor;MLOps+CIE+2026;BMS+College+of+Engineering" alt="Typing SVG" />

<br/>

![MLOps](https://img.shields.io/badge/MLOps-CIE%202026-00d4ff?style=for-the-badge&logoColor=white)
![USN](https://img.shields.io/badge/USN-1BM23AI016-7f5af0?style=for-the-badge)
![Status](https://img.shields.io/badge/Repo-PUBLIC-00ff9d?style=for-the-badge)
![Marks](https://img.shields.io/badge/Total-30%20Marks-ffa500?style=for-the-badge)

<br/>

> **SLA enforcement & capacity planning via ML pipeline**
> BMS College of Engineering · Dept. of Machine Learning · Even Sem 2026

</div>

---

## 📋 Exam Info

| Field | Details |
|---|---|
| 🎓 Course | MLOps — 24AM6AEMLO |
| 📄 Paper Code | mlops-cie-013 |
| 🪪 USN | 1BM23AI016 |
| 📅 Date | 04 May 2026 |
| 🏫 College | BMS College of Engineering |

---

## 🚀 Pipeline

[ MLflow Tracking ] ──▶ [ Hyperparameter Tuning ] ──▶ [ Docker Packaging ] ──▶ [ FastAPI Serving ]
Task 1                     Task 2                      Task 3                   Task 4

---

## 📊 Dataset · `training_data.csv` · 25 samples

| Feature | Range | Type |
|---|---|---|
| `request_size_kb` | 1 – 500 | float |
| `server_load` | 0.1 – 1.0 | float |
| `is_cached` | 0 – 1 | int |
| `region_latency` | 10 – 200 | float |
| ⭐ `response_time_ms` | **TARGET** | float |

---

## ✅ Tasks

| # | Task | Details | Marks | Output |
|---|---|---|---|---|
| 1 | 📈 Experiment Tracking | Ridge + GradientBoosting · MLflow · Best by RMSE | 6 | `step1_s1.json` |
| 2 | 🔧 Hyperparameter Tuning | GridSearchCV 5-fold · Nested MLflow runs | 8 | `step2_s2.json` |
| 3 | 🐳 Docker Packaging | `cloudpulse-predictor:v1` · python:3.12-slim | 8 | `step3_s3.json` |
| 4 | ⚡ FastAPI Serving | POST /score · GET /ping · Port 9000 | 8 | `step4_s4.json` |

---

## 🗂️ Repository Structure
Internals_Basics/
└── MLOPs_Lab_CIE/
├── 📁 data/
│   └── training_data.csv
├── 📁 src/
│   ├── train.py
│   ├── tune.py
│   ├── predict_cli.py
│   └── api.py
├── 📁 models/
│   └── best_model.pkl
├── 📁 results/
│   ├── step1_s1.json
│   ├── step2_s2.json
│   ├── step3_s3.json
│   └── step4_s4.json
├── requirements.txt
├── Dockerfile
└── .gitignore

---

## 🛠️ Tech Stack

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-00d4ff?style=for-the-badge&logoColor=white)

---

## ⚡ Quickstart

```bash
# Clone & setup
git clone https://github.com/YOUR_USERNAME/Internals_Basics.git
cd Internals_Basics/MLOPs_Lab_CIE
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Task 1 — MLflow tracking
python src/train.py

# Task 2 — Hyperparameter tuning
python src/tune.py

# Task 3 — Docker
docker build -t cloudpulse-predictor:v1 .
docker run cloudpulse-predictor:v1 --request_size_kb 175.7 --server_load 0.4 --is_cached 0 --region_latency 132

# Task 4 — FastAPI
uvicorn src.api:app --port 9000
curl -X POST http://localhost:9000/score \
  -H "Content-Type: application/json" \
  -d '{"request_size_kb":175.7,"server_load":0.4,"is_cached":0,"region_latency":132}'
```

---

<div align="center">

BMS College of Engineering · Dept. of Machine Learning · Even Sem 2026

![GitHub](https://img.shields.io/badge/Internals__Basics-PUBLIC-00ff9d?style=flat-square&logo=github)

</div>
