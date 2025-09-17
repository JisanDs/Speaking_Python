import json

def load_json(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
        
