import argparse
import time
import datetime
import threading
import logging
from utils import parse_timestamps, make_api_call

# Global API URL
API_URL = "https://ifconfig.co"

# Setup logging
logging.basicConfig(
    filename="api_calls.log",
    level=logging.INFO,
    format="%(asctime)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def schedule_api_calls(timestamps_dict):
    now = datetime.datetime.now()
    for ts, instances in timestamps_dict.items():
        target_time = datetime.datetime.combine(now.date(), datetime.datetime.strptime(ts, "%H:%M:%S").time())
        delay = (target_time - now).total_seconds()
        if delay < 0:
            logging.warning(f"Skipped past timestamp: {ts}")
            continue

        threading.Timer(delay, execute_concurrent_calls, [instances]).start()

def execute_concurrent_calls(instances):
    threads = []
    for _ in instances:
        t = threading.Thread(target=make_api_call, args=(API_URL,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Schedule API calls based on timestamps.")
    parser.add_argument("Timestamps", type=str, help="Comma-separated timestamps (HH:MM:SS)")
    args = parser.parse_args()

    timestamps_dict = parse_timestamps(args.Timestamps)
    schedule_api_calls(timestamps_dict)

    # Keep the script running
    while True:
        time.sleep(1)
