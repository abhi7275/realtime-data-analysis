import time
import random
import json
import requests
from datetime import datetime

API_URL = "http://fastapi:8000/ingest"

def generate_sensor_data():
    device_id = f"device_{random.randint(1, 10)}"
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    temperature = random.uniform(60.0, 85.0)
    vibration = random.uniform(0.01, 0.1)
    pressure = random.uniform(1.0, 1.5)
    failure = random.choice([0, 1])
    return {
        "device_id": device_id,
        "timestamp": timestamp,
        "temperature": temperature,
        "vibration": vibration,
        "pressure": pressure,
        "failure": failure
    }

def send_data_to_api(data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 200:
            print(f"Data sent successfully: {data}")
        else:
            print(f"Failed to send data: {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

def run_simulation():
    while True:
        sensor_data = generate_sensor_data()
        send_data_to_api(sensor_data)
        time.sleep(1)

if __name__ == "__main__":
    run_simulation()
