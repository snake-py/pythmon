## Core libraries
import os
import json

## Error Imports 
from json.decoder import JSONDecodeError


default_configs = {
    "PYTHMON_WATCH_PATH": "./",
    "PYTHMON_RUN": "python main.py",
    "PYTHMON_IGNORE": ["^.*.pyc$", "^__pycache__"]
}

def get_configs():
    if os.path.isfile(f"{os.getcwd()}/pythmon.json"):
            
        with open(f"{os.getcwd()}/pythmon.json") as json_config:
            try:
                return json.load(json_config)
            except JSONDecodeError:
                print("---- WARNING ----")
    print("PYTHMON IS running on default settings.")
    return default_configs


if __name__ == '__main__':
    print(os.getcwd())