## Core libraries
import json

## Error Imports 
from json.decoder import JSONDecodeError


default_configs = {
    "PYTHMON_WATCH_PATH": "./",
    "PYTHMON_RUN": "python main.py",
    "PYTHMON_IGNORE": ["^.*.pyc$", "^__pycache__"]
}

def get_configs():
    with open("./pythmon.json") as json_config:
        try:
            return json.load(json_config)
        except JSONDecodeError:
            print("---- WARNING ----")
            print("PYTHMON IS running on default settings since you pythmon.json is not correct.")
            return default_configs



configs = get_configs()