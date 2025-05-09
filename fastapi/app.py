from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class SensorData(BaseModel):
    device_id: str
    timestamp: str
    temperature: float
    vibration: float
    pressure: float
    failure: int

@app.post('/ingest')
def ingest_data(data: SensorData):
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensor_data (device_id, timestamp, temperature, vibration, pressure, failure) VALUES (%s, %s, %s, %s, %s, %s)", (data.device_id, data.timestamp, data.temperature, data.vibration, data.pressure, data.failure))
    conn.commit()
    cursor.close()
    conn.close()
    return {'message': 'Data ingested successfully!'}
