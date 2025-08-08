import sqlite3
from datetime import datetime
import os

DB_PATH = "logs/predictions.db"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Initialize DB if not exists
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sepal_length REAL,
                sepal_width REAL,
                petal_length REAL,
                petal_width REAL,
                prediction TEXT,
                timestamp TEXT
            )
        ''')
        conn.commit()

def log_prediction(data: dict, prediction: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO predictions (sepal_length, sepal_width, petal_length, petal_width, prediction, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            data["sepal_length"],
            data["sepal_width"],
            data["petal_length"],
            data["petal_width"],
            prediction,
            datetime.utcnow().isoformat()
        ))
        conn.commit()
