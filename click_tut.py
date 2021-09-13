import click

# @click.command()
# @click.argument('name')
# @click.option('--number', type=int, help="Help message for option")
# def main(name, number):
#     """
#     Help Mesage
#     """
#     for _ in range(number):
#         print(f"Hello {name}")


# @click.command()
# @click.option('--weather', type=click.Choice(['sunny', 'rainy', 'snowy']))
# def main(weather):
#     """
#     Help Mesage
#     """
#     print(f"I love it when the weather is {weather}")


## Use groups


@click.group()
def cli():
    pass

@cli.group()
def lunch():
    pass


@cli.group()
def dinner():
    pass


# @click.command()
# def burger():
#     print(f"Enjoy your burger")


# lunch.add_command(burger)
# dinner.add_command(burger)


@lunch.command()
# @dinner.command() ## it is not possible to use this wy to add a function to multiple commands
def burger():
    print(f"Enjoy your burger")


dinner.add_command(burger)


if __name__ == "__main__":
    cli()