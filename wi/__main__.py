import wcore_py
import click
from pathlib import Path

def get_next_input():
    return "\n".join(iter(lambda: input("# ").strip(), ""))

@click.group()
def cli():
    pass

@cli.command()
@click.argument('path')
def run(path: str) -> None:
    with open(str(Path('.')/path)) as f:
        content = f.read()

    wcore_py.eval(content)

@cli.command()
def shell() -> None:
    state = wcore_py.State()

    while (code_block := get_next_input()) != "exit":
        state.apply(code_block)

if __name__ == "__main__":
    cli()
