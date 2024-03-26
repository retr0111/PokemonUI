import json
import os

DATA_FILE = "pokeapi_data.json"

def save_data_to_json(data):
    with open(DATA_FILE, "w") as json_file:
        json.dump(data, json_file)

def load_data_from_json():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as json_file:
            return json.load(json_file)
    return None
