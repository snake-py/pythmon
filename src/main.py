## Ultimately in output
import os
import sys
import shutil
import click
from rich import print as richPrint
from rich.console import Console
from watchdog.observers.polling import PollingObserver as Observer
from settings import get_configs

console = Console()
## Own
from output import greeting
from observer import make_event_handler


@click.group()
def main():
    pass

@main.command()
def help():
    print("some help")

@main.command()
@click.option("--script", default=None)
def observe(script):
    """
    Will start to watch script
    """
    configs = get_configs()
    # Make Eventhandler    
    event_handler = make_event_handler(script=script, configs=configs)
    # Create Observer and start watching
    observer = Observer()
    print(observe)
    observer.schedule(event_handler, path=configs["PYTHMON_WATCH_PATH"], recursive=False)
    observer.start()
        
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("Stopping PythMon")
            observer.stop()

@main.command(name="configs:make")
def make():
    shutil.copy(f"{os.path.dirname(os.path.realpath(sys.argv[0]))}/pythmon.example.json", f"{os.getcwd()}/pythmon.json")

@main.command(name="configs:read")
def read():
    richPrint("Read configs... ")



if __name__ == "__main__":
    main()
