import json
import os

DB_FILE = "data.json"

def load_data():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump({"users": {}}, f)
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def signup(username, password):
    data = load_data()
    if username in data["users"]:
        return False
    data["users"][username] = {"password": password, "high_score": 0}
    save_data(data)
    return True

def login(username, password):
    data = load_data()
    return username in data["users"] and data["users"][username]["password"] == password

def update_score(username, score):
    data = load_data()
    if score > data["users"][username]["high_score"]:
        data["users"][username]["high_score"] = score
        save_data(data)

def get_high_score(username):
    data = load_data()
    return data["users"].get(username, {}).get("high_score", 0)
