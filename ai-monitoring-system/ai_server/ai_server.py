from flask import Flask, request
import os
import datetime
import json

app = Flask(__name__)

LOG_FILE = "/tmp/ai.log"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json

    # Pretty print alert in console
    print("Received Alert:\n", json.dumps(data, indent=2))

    # Extract useful info
    alertname = data.get("commonLabels", {}).get("alertname", "Unknown")
    instance = data.get("commonLabels", {}).get("instance", "Unknown")
    status = data.get("status", "unknown")

    # Log entry with timestamp
    log_entry = f"{datetime.datetime.now()} | {alertname} | {instance} | {status}\n"

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    # 🔧 Auto-healing logic
    if alertname == "HighCPUUsage" and status == "firing":
        print("⚙️ Taking action: Killing high CPU process...")
        os.system("pkill yes")   # Example action

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)