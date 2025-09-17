"""This library contains basic but useful file operations function."""

import json

def load_json(filename):
    """This function load json file and json file not exist or file empty it's return a new dict."""
    try:
        with open(filename) as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}
        
