# Timestamp Scheduler

## 📌 Description

This script takes a list of timestamps and schedules HTTP API calls to `https://ifconfig.co` at the exact time. If multiple calls occur at the same second, they are executed concurrently.

## ✅ Features

- Accepts command-line input for timestamps.
- Makes precise second-level API calls.
- Supports concurrent execution.
- Logs every API call (success/failure).
- Modular code with tests.

## 🛠 Requirements

- Python 3.x

## ▶️ How to Run

```bash
python scheduler.py "09:15:25,11:58:23,13:45:09,13:45:09,13:45:09,17:22:00,17:22:00"
