## Ultimately in output
import click
from rich import print as richPrint
from rich.console import Console
from watchdog.observers.polling import PollingObserver as Observer


console = Console()
## Own
from output import greeting
from observer import make_event_handler


@click.group()
def cli():
    pass
    

# @cli.command()
@click.command()
@click.option("--script", default="PYTHMON_RUN")
def observe(script):
    """
    Will start to watch script
    """
    # Make Eventhandler    
    if script != "PYTHMON_RUN":
        richPrint(f"PythMon is using this script: {script}")
        pass
    else:
        richPrint(f"PythMon runs in default mode.")
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

cli.add_command(observe)

@cli.group()
def configs():
    pass

@configs.command()
def make():
    richPrint("Making configs... ")


if __name__ == "__main__":
    cli()
