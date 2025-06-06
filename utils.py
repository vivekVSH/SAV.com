from collections import defaultdict
import urllib.request
import logging

def parse_timestamps(timestamp_str):
    timestamps = timestamp_str.split(",")
    timestamp_groups = defaultdict(list)
    for ts in timestamps:
        ts = ts.strip()
        if ts:
            timestamp_groups[ts].append(ts)
    return dict(timestamp_groups)  # Fixed: return regular dict for test compatibility

def make_api_call(api_url):
    try:
        with urllib.request.urlopen(api_url) as response:
            ip = response.read().decode().strip()
            logging.info(f"Successfully called API at {api_url} | IP: {ip}")
    except Exception as e:
        logging.error(f"Failed to call API at {api_url}: {e}")
