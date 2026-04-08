# ⚙️ Complete Setup Guide

## 📌 Prerequisites

* Linux server (Rocky / Ubuntu)
* Python3 installed
* Internet access

---

## 🔹 Step 1: Install Node Exporter

```bash
wget https://github.com/prometheus/node_exporter/releases/download/v*/node_exporter-*.tar.gz
tar -xvf node_exporter-*.tar.gz
cd node_exporter-*
./node_exporter &
```

---

## 🔹 Step 2: Install Prometheus

```bash
wget https://github.com/prometheus/prometheus/releases/download/v*/prometheus-*.tar.gz
tar -xvf prometheus-*.tar.gz
cd prometheus-*
```

### Configure `prometheus.yml`

```yaml
scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
```

### Add alert rules

```yaml
rule_files:
  - "rules.yml"
```

---

## 🔹 Step 3: Create Alert Rules (`rules.yml`)

```yaml
groups:
- name: cpu-alert
  rules:
  - alert: HighCPUUsage
    expr: 100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100) > 80
    for: 1m
    labels:
      severity: warning
    annotations:
      summary: "High CPU usage detected"
```

---

## 🔹 Step 4: Setup Alertmanager

```bash
wget https://github.com/prometheus/alertmanager/releases/download/v*/alertmanager-*.tar.gz
tar -xvf alertmanager-*.tar.gz
cd alertmanager-*
```

### Configure `alertmanager.yml`

* Add Gmail SMTP
* Add webhook URL

---

## 🔹 Step 5: Fix Gmail SMTP Issue

* Enable 2FA in Gmail
* Generate App Password
* Use App Password in config

---

## 🔹 Step 6: Setup AI Engine

```bash
cd ai_server
pip install -r requirements.txt
python3 ai_server.py
```

---

## 🔹 Step 7: Install Grafana

```bash
sudo dnf install grafana -y
sudo systemctl start grafana
```

* Open: http://localhost:3000
* Add Prometheus datasource
* Import Node Exporter dashboard

---

## 🔹 Step 8: Start Services

```bash
./prometheus --config.file=prometheus.yml &
./alertmanager --config.file=alertmanager.yml &
```

---

## 🔹 Step 9: Test Alert

```bash
yes > /dev/null &
```

---

## ✅ Expected Output

* Grafana shows CPU spike
* Alertmanager sends email
* Flask receives alert
* Auto-healing triggers

---

## 🛑 Stop CPU Test

```bash
pkill yes
```