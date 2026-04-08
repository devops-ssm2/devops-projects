#!/bin/bash
curl -X POST http://localhost:5001/alert \
-H "Content-Type: application/json" \
-d '{"alertname": "HighCPUUsage"}'