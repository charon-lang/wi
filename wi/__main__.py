import wcore_py
import click
from pathlib import Path

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path')
def run(path: str) -> None:
    with open(str(Path('.')/path)) as f:
        content = f.read()

    wcore_py.eval(content)

if __name__ == "__main__":
    cli()
