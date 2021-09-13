from pyfiglet import Figlet
from rich.console import Console

console = Console()

def greeting():
    f = Figlet(font='slant')
    console.print(f.renderText('PythMon'), style="bold red" )
    console.print("""
PythMon is a CLI tool build on top of watchdog. I coded it as an simple equivalent to nodemon. 
My original intention was that I have very lightweight VMs, which do not have node installed,
however I still required to watch files. 
    """)
    console.print("Type [bold]pythmon -h[/bold] for help!")





# from rich import print as richPrint
# from rich.console import Console
# ## Make configs 


# richPrint("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())
# console = Console()
# console.print("Hello", "World!", style="bold red")
# console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# test_data = [
#     {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1",},
#     {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
#     {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
# ]

# def test_log():
#     enabled = False
#     context = {
#         "foo": "bar",
#     }
#     movies = ["Deadpool", "Rise of the Skywalker"]
#     console.log("Hello from", console, "!")
#     console.log(test_data, log_locals=True)


# test_log()
# console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon:")

# from rich.syntax import Syntax

# my_code = '''
# def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
#     """Iterate and generate a tuple with a flag for first and last value."""
#     iter_values = iter(values)
#     try:
#         previous_value = next(iter_values)
#     except StopIteration:
#         return
#     first = True
#     for value in iter_values:
#         yield first, False, previous_value
#         first = False
#         previous_value = value
#     yield first, True, previous_value
# '''
# syntax = Syntax(my_code, "python", theme="monokai", line_numbers=True)
# console = Console()
# console.print(syntax)
