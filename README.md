cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CloudPulse MLOps</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');
  *{box-sizing:border-box;margin:0;padding:0}
  :root{--cp-bg:#04080f;--cp-surface:#0a1120;--cp-border:#1a2a40;--cp-accent:#00d4ff;--cp-accent2:#7f5af0;--cp-green:#00ff9d;--cp-text:#e8f0fe;--cp-muted:#6b7a99;--cp-card:#0d1829}
  body{background:var(--cp-bg);color:var(--cp-text);font-family:'Syne',sans-serif;min-height:100vh}
  .wrap{max-width:700px;margin:0 auto;padding:2rem 1.5rem}
  .hero{border:1px solid var(--cp-border);border-radius:16px;background:var(--cp-surface);padding:2rem;margin-bottom:1.5rem;position:relative;overflow:hidden}
  .hero::before{content:'';position:absolute;top:-60px;right:-60px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(0,212,255,0.12) 0%,transparent 70%);pointer-events:none}
  .hero::after{content:'';position:absolute;bottom:-40px;left:-40px;width:160px;height:160px;border-radius:50%;background:radial-gradient(circle,rgba(127,90,240,0.10) 0%,transparent 70%);pointer-events:none}
  .badge-row{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:1rem}
  .badge{font-family:'Space Mono',monospace;font-size:10px;padding:3px 10px;border-radius:20px;border:1px solid;letter-spacing:0.08em}
  .badge-blue{border-color:var(--cp-accent);color:var(--cp-accent);background:rgba(0,212,255,0.07)}
  .badge-purple{border-color:var(--cp-accent2);color:var(--cp-accent2);background:rgba(127,90,240,0.07)}
  .badge-green{border-color:var(--cp-green);color:var(--cp-green);background:rgba(0,255,157,0.07)}
  .hero-title{font-size:2rem;font-weight:800;letter-spacing:-0.02em;line-height:1.1;margin-bottom:0.5rem}
  .hero-title span{color:var(--cp-accent)}
  .hero-sub{font-size:0.85rem;color:var(--cp-muted);font-family:'Space Mono',monospace;line-height:1.6}
  .meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:1.2rem}
  .meta-item{background:rgba(0,212,255,0.04);border:1px solid var(--cp-border);border-radius:8px;padding:10px 14px}
  .meta-label{font-size:10px;color:var(--cp-muted);font-family:'Space Mono',monospace;letter-spacing:0.1em;margin-bottom:3px}
  .meta-val{font-size:13px;font-weight:700;color:var(--cp-text)}
  .section{margin-bottom:1.5rem}
  .section-header{display:flex;align-items:center;gap:10px;margin-bottom:1rem}
  .section-num{font-family:'Space Mono',monospace;font-size:10px;color:var(--cp-accent);background:rgba(0,212,255,0.08);border:1px solid rgba(0,212,255,0.2);border-radius:4px;padding:2px 8px;letter-spacing:0.1em}
  .section-title{font-size:1rem;font-weight:700;letter-spacing:0.02em}
  .ds-table{width:100%;border-collapse:collapse;font-family:'Space Mono',monospace;font-size:12px}
  .ds-table th{text-align:left;padding:8px 12px;color:var(--cp-muted);font-weight:400;border-bottom:1px solid var(--cp-border);letter-spacing:0.08em;font-size:10px}
  .ds-table td{padding:9px 12px;border-bottom:1px solid rgba(26,42,64,0.6);color:var(--cp-text)}
  .ds-table tr:last-child td{border-bottom:none}
  .ds-table td:last-child{color:var(--cp-accent);font-size:11px}
  .target-row td{color:var(--cp-green)!important}
  .table-wrap{border:1px solid var(--cp-border);border-radius:10px;overflow:hidden;background:var(--cp-card)}
  .tasks-grid{display:grid;gap:10px}
  .task-card{border:1px solid var(--cp-border);border-radius:10px;background:var(--cp-card);padding:14px 16px;display:flex;align-items:flex-start;gap:14px;transition:border-color 0.2s}
  .task-card:hover{border-color:rgba(0,212,255,0.3)}
  .task-icon{width:36px;height:36px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px}
  .t1{background:rgba(0,212,255,0.1);border:1px solid rgba(0,212,255,0.2)}
  .t2{background:rgba(127,90,240,0.1);border:1px solid rgba(127,90,240,0.2)}
  .t3{background:rgba(0,255,157,0.1);border:1px solid rgba(0,255,157,0.2)}
  .t4{background:rgba(255,165,0,0.1);border:1px solid rgba(255,165,0,0.2)}
  .task-body{flex:1}
  .task-title{font-size:13px;font-weight:700;margin-bottom:4px}
  .task-desc{font-size:12px;color:var(--cp-muted);line-height:1.5;font-family:'Space Mono',monospace}
  .task-marks{margin-left:auto;font-family:'Space Mono',monospace;font-size:11px;color:var(--cp-accent);white-space:nowrap;padding:2px 8px;background:rgba(0,212,255,0.06);border:1px solid rgba(0,212,255,0.15);border-radius:20px;align-self:flex-start}
  .tree{font-family:'Space Mono',monospace;font-size:12px;line-height:2;color:var(--cp-text);background:var(--cp-card);border:1px solid var(--cp-border);border-radius:10px;padding:16px 20px}
  .tree .folder{color:var(--cp-accent)}
  .tree .file{color:var(--cp-muted)}
  .tree .highlight{color:var(--cp-green)}
  .code-block{background:var(--cp-card);border:1px solid var(--cp-border);border-radius:10px;padding:14px 16px;font-family:'Space Mono',monospace;font-size:11px;line-height:1.8;color:#8eb8e0;overflow-x:auto;margin-bottom:8px}
  .code-block .cmd{color:var(--cp-green)}
  .code-block .comment{color:var(--cp-muted)}
  .code-label{font-family:'Space Mono',monospace;font-size:10px;color:var(--cp-muted);letter-spacing:0.1em;margin-bottom:6px}
  .pipeline{display:flex;align-items:center;gap:0;margin:4px 0}
  .pipe-step{flex:1;text-align:center;padding:10px 6px;border:1px solid var(--cp-border);background:var(--cp-card);font-size:11px;font-weight:700;letter-spacing:0.04em}
  .pipe-step:first-child{border-radius:8px 0 0 8px}
  .pipe-step:last-child{border-radius:0 8px 8px 0}
  .pipe-arrow{color:var(--cp-accent);font-size:14px;flex-shrink:0}
  .p1{color:var(--cp-accent);border-color:rgba(0,212,255,0.3)}
  .p2{color:var(--cp-accent2);border-color:rgba(127,90,240,0.3)}
  .p3{color:var(--cp-green);border-color:rgba(0,255,157,0.3)}
  .p4{color:#ffa500;border-color:rgba(255,165,0,0.3)}
  .pipe-sub{font-size:9px;font-family:'Space Mono',monospace;color:var(--cp-muted);font-weight:400;display:block;margin-top:2px}
  .footer{border-top:1px solid var(--cp-border);padding-top:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px}
  .footer-left{font-family:'Space Mono',monospace;font-size:10px;color:var(--cp-muted)}
  .footer-right{font-family:'Space Mono',monospace;font-size:10px;color:var(--cp-accent)}
  .divider{height:1px;background:var(--cp-border);margin:1.5rem 0}
  .logo-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:1rem}
  .logo-pill{display:flex;align-items:center;gap:6px;padding:5px 12px;border-radius:20px;border:1px solid var(--cp-border);background:rgba(255,255,255,0.02);font-size:11px;font-family:'Space Mono',monospace;color:var(--cp-muted)}
  .logo-dot{width:8px;height:8px;border-radius:50%}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <div class="badge-row">
      <span class="badge badge-blue">MLOps</span>
      <span class="badge badge-purple">CIE 2026</span>
      <span class="badge badge-green">PUBLIC REPO</span>
    </div>
    <div class="hero-title">Cloud<span>Pulse</span><br>Response Predictor</div>
    <div class="hero-sub" style="margin-top:8px">SLA enforcement &amp; capacity planning via ML pipeline<br>BMS College of Engineering · Dept. of Machine Learning</div>
    <div class="meta-grid">
      <div class="meta-item"><div class="meta-label">USN</div><div class="meta-val">1BM23AI016</div></div>
      <div class="meta-item"><div class="meta-label">Paper Code</div><div class="meta-val">mlops-cie-013</div></div>
      <div class="meta-item"><div class="meta-label">Course Code</div><div class="meta-val">24AM6AEMLO</div></div>
      <div class="meta-item"><div class="meta-label">Date</div><div class="meta-val">04 May 2026</div></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header">
      <span class="section-num">PIPELINE</span>
      <span class="section-title">End-to-End MLOps Flow</span>
    </div>
    <div class="pipeline">
      <div class="pipe-step p1">Track<span class="pipe-sub">MLflow</span></div>
      <div class="pipe-arrow">›</div>
      <div class="pipe-step p2">Tune<span class="pipe-sub">GridSearch</span></div>
      <div class="pipe-arrow">›</div>
      <div class="pipe-step p3">Package<span class="pipe-sub">Docker</span></div>
      <div class="pipe-arrow">›</div>
      <div class="pipe-step p4">Serve<span class="pipe-sub">FastAPI</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-header">
      <span class="section-num">DATASET</span>
      <span class="section-title">training_data.csv · 25 samples</span>
    </div>
    <div class="table-wrap">
      <table class="ds-table">
        <thead><tr><th>FEATURE</th><th>RANGE</th><th>TYPE</th></tr></thead>
        <tbody>
          <tr><td>request_size_kb</td><td>1 – 500</td><td>float</td></tr>
          <tr><td>server_load</td><td>0.1 – 1.0</td><td>float</td></tr>
          <tr><td>is_cached</td><td>0 – 1</td><td>int</td></tr>
          <tr><td>region_latency</td><td>10 – 200</td><td>float</td></tr>
          <tr class="target-row"><td>response_time_ms ★</td><td>target</td><td>float</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="section">
    <div class="section-header">
      <span class="section-num">TASKS</span>
      <span class="section-title">4 Tasks · 30 Marks Total</span>
    </div>
    <div class="tasks-grid">
      <div class="task-card">
        <div class="task-icon t1">◈</div>
        <div class="task-body">
          <div class="task-title">Task 1 — Experiment Tracking</div>
          <div class="task-desc">Train Ridge + GradientBoosting · Log MAE/RMSE to MLflow · Select best by RMSE · results/step1_s1.json</div>
        </div>
        <div class="task-marks">6 marks</div>
      </div>
      <div class="task-card">
        <div class="task-icon t2">⬡</div>
        <div class="task-body">
          <div class="task-title">Task 2 — Hyperparameter Tuning</div>
          <div class="task-desc">GridSearchCV 5-fold · n_estimators/lr/depth grid · Nested MLflow runs · results/step2_s2.json</div>
        </div>
        <div class="task-marks">8 marks</div>
      </div>
      <div class="task-card">
        <div class="task-icon t3">⬢</div>
        <div class="task-body">
          <div class="task-title">Task 3 — Docker Packaging</div>
          <div class="task-desc">python:3.12-slim · predict_cli.py via argparse · Image: cloudpulse-predictor:v1 · results/step3_s3.json</div>
        </div>
        <div class="task-marks">8 marks</div>
      </div>
      <div class="task-card">
        <div class="task-icon t4">◎</div>
        <div class="task-body">
          <div class="task-title">Task 4 — FastAPI Serving</div>
          <div class="task-desc">POST /score · GET /ping · Port 9000 · Pydantic validation · HTTP 422 on bad input · results/step4_s4.json</div>
        </div>
        <div class="task-marks">8 marks</div>
      </div>
    </div>
  </div>
  <div class="section">
    <div class="section-header">
      <span class="section-num">STRUCTURE</span>
      <span class="section-title">Repository Layout</span>
    </div>
    <div class="tree">
<span class="folder">Internals_Basics/</span>
└── <span class="folder">MLOPs_Lab_CIE/</span>
    ├── <span class="folder">data/</span>
    │   └── <span class="highlight">training_data.csv</span>
    ├── <span class="folder">src/</span>
    │   ├── <span class="highlight">train.py</span>
    │   ├── <span class="highlight">tune.py</span>
    │   ├── <span class="highlight">predict_cli.py</span>
    │   └── <span class="highlight">api.py</span>
    ├── <span class="folder">models/</span>  <span class="file">← best_model.pkl</span>
    ├── <span class="folder">results/</span>
    │   ├── <span class="highlight">step1_s1.json</span>
    │   ├── <span class="highlight">step2_s2.json</span>
    │   ├── <span class="highlight">step3_s3.json</span>
    │   └── <span class="highlight">step4_s4.json</span>
    ├── <span class="highlight">requirements.txt</span>
    ├── <span class="highlight">Dockerfile</span>
    └── <span class="highlight">.gitignore</span>
    </div>
  </div>
  <div class="section">
    <div class="section-header">
      <span class="section-num">QUICKSTART</span>
      <span class="section-title">Run the Pipeline</span>
    </div>
    <div class="code-label">// SETUP</div>
    <div class="code-block">
<span class="cmd">git clone</span> https://github.com/YOUR_USERNAME/Internals_Basics.git
<span class="cmd">cd</span> Internals_Basics/MLOPs_Lab_CIE
<span class="cmd">python -m venv</span> venv &amp;&amp; <span class="cmd">source</span> venv/bin/activate
<span class="cmd">pip install</span> -r requirements.txt
    </div>
    <div class="code-label">// TASKS</div>
    <div class="code-block">
<span class="cmd">python</span> src/train.py          <span class="comment"># Task 1 — MLflow tracking</span>
<span class="cmd">python</span> src/tune.py           <span class="comment"># Task 2 — Hyperparameter tuning</span>
<span class="cmd">docker build</span> -t cloudpulse-predictor:v1 .  <span class="comment"># Task 3 — Docker</span>
<span class="cmd">uvicorn</span> src.api:app --port 9000             <span class="comment"># Task 4 — FastAPI</span>
    </div>
    <div class="code-label">// TEST API</div>
    <div class="code-block">
<span class="cmd">curl</span> http://localhost:9000/ping
<span class="cmd">curl</span> -X POST http://localhost:9000/score \
  -H <span class="highlight">"Content-Type: application/json"</span> \
  -d <span class="highlight">'{"request_size_kb":175.7,"server_load":0.4,"is_cached":0,"region_latency":132}'</span>
    </div>
  </div>
  <div class="section">
    <div class="section-header">
      <span class="section-num">STACK</span>
      <span class="section-title">Technologies Used</span>
    </div>
    <div class="logo-row">
      <div class="logo-pill"><div class="logo-dot" style="background:#0194e2"></div>scikit-learn</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#0fb8e0"></div>MLflow</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#2496ed"></div>Docker</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#009688"></div>FastAPI</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#f7c948"></div>pandas</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#4dabf7"></div>numpy</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#7f5af0"></div>joblib</div>
      <div class="logo-pill"><div class="logo-dot" style="background:#00d4ff"></div>uvicorn</div>
    </div>
  </div>
  <div class="divider"></div>
  <div class="footer">
    <div class="footer-left">BMS College of Engineering · ML Dept · Even Sem 2026</div>
    <div class="footer-right">repo: Internals_Basics · PUBLIC</div>
  </div>
</div>
</body>
</html>
EOF
