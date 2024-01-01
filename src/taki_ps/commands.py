import typer

cli = typer.Typer()


@cli.command()
def init_env():
    print("Starting...")


@cli.command()
def validate():
    print("Validating...")


if __name__ == "__main__":
    cli()
