## Core
import os
import inspect

## third party
from watchdog.events import RegexMatchingEventHandler

## own modules
from settings import configs, default_configs


class PythMonHandler(RegexMatchingEventHandler):
    def __init__(self, script,  regexes, ignore_regexes, ignore_directories, case_sensitive):
        self.script = script
        super().__init__(regexes=regexes, ignore_regexes=ignore_regexes, ignore_directories=ignore_directories, case_sensitive=case_sensitive)
    
    def on_any_event(self, event):
        print(event.event_type, event.src_path)
        if not self.script:
            pass
        else:
            os.system(configs["script"][self.script][inspect.stack[0][3]])

    def on_modified(self, event):
        if not self.script:
            os.system(configs["PYTHMON_RUN"])
        else:
            os.system(configs["script"][self.script][inspect.stack[0][3]])

    def on_created(self, event):
        if not self.script:
            pass
        else:
            os.system(configs["script"][self.script][inspect.stack[0][3]])

    def on_deleted(self, event):
        if not self.script:
            pass
        else:
            os.system(configs["script"][self.script][inspect.stack[0][3]])

    def on_moved(self, event):
        if not self.script:
            pass
        else:
            os.system(configs["script"][self.script][inspect.stack[0][3]])

def make_event_handler(script):
    try:
        ignore_patterns = configs["PYTHMON_IGNORE"]
    except KeyError:
        ignore_patterns = default_configs["PYTHMON_IGNORE"]
    ignore_directories = True
    case_sensitive = True
    return  PythMonHandler(script, regexes=None, ignore_regexes=ignore_patterns, ignore_directories=ignore_directories, case_sensitive=case_sensitive)