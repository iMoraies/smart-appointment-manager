# app/storage.py
import json
from pathlib import Path

DATABASE_PATH = Path("data/database.json")


def load_data():
    if not DATABASE_PATH.exists():
        return {
            "clients": [],
            "services": []
        }

    with open(DATABASE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    DATABASE_PATH.parent.mkdir(exist_ok=True)

    with open(DATABASE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
