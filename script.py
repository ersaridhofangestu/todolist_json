import json
import os

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file :
            return json.load(file)
    return []

def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)