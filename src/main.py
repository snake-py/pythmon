## Ultimately in output
import click
from rich import print as richPrint
from rich.console import Console
from watchdog.observers.polling import PollingObserver as Observer
from settings import configs

console = Console()
## Own
from output import greeting
from observer import make_event_handler


@click.group()
def cli():
    print("Runner ... ")

@click.command()
def help():
    print("sone helo")

# @cli.command()
@click.command()
@click.option("--script", default=None)
def observe(script):
    """
    Will start to watch script
    """
    # Make Eventhandler    
    event_handler = make_event_handler(script=script)
    # Create Observer and start watching
    observer = Observer()
    print(observe)
    observer.schedule(event_handler, path=configs["PYTHMON_WATCH_PATH"], recursive=True)
    observer.start()
        
    while True:
        try:
            pass
        except KeyboardInterrupt:
            print("Stopping PythMon")
            observer.stop()

cli.add_command(observe)

# @cli.group()
# def configs():
#     pass

# @configs.command()
# def make():
#     richPrint("Making configs... ")

# @configs.command()
# def read():
#     richPrint("Read configs... ")

if __name__ == "__main__":
    cli()
