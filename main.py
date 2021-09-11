## Core libraries
import os
import json

## Third Partie Libraries
from watchdog.observers.polling import PollingObserver as Observer
from watchdog.events import RegexMatchingEventHandler

## Error Imports 
from json.decoder import JSONDecodeError


## Make configs 

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

class PythHandler(RegexMatchingEventHandler):
    
    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_modified(self, event):
        print("Trigger Command")
        os.system(configs["PYTHMON_RUN"])

    def on_created(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_moved(self, event):
        pass

def make_event_handler():
    try:
        ignore_patterns = configs["PYTHMON_IGNORE"]
    except KeyError:
        ignore_patterns = default_configs["PYTHMON_IGNORE"]

    ignore_directories = True
    case_sensitive = True
    return  PythHandler(ignore_regexes=ignore_patterns, ignore_directories=ignore_directories, case_sensitive=case_sensitive)


if __name__ == "__main__":
    # Make Eventhandler    
    event_handler = make_event_handler()

    # Create Observer and start watching
    observer = Observer()
    observer.schedule(event_handler, path=configs["PYTHMON_WATCH_PATH"], recursive=True)
    observer.start()
        
    while True:
        try:
            pass
        except KeyboardInterrupt:
            observer.stop()