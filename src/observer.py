## Core
import os

## third party
from watchdog.events import RegexMatchingEventHandler

## own modules
from settings import configs, default_configs


class PythMonHandler(RegexMatchingEventHandler):
    
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
    return  PythMonHandler(ignore_regexes=ignore_patterns, ignore_directories=ignore_directories, case_sensitive=case_sensitive)