from pathlib import Path
import click

@click.command()
@click.option('--hidden/--no-hidden', default=False, show_default=True, help="show hidden files and folders")
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def pytree(directory : Path, hidden : bool):
    """ converts the input directory into a readable filetree"""
    click.echo(directory)
    d = Path(directory)
    printDirContents(d, show_hidden=hidden)

def printDirContents(d : Path, level=0, show_hidden=False):
    for node in d.glob("./*"):
        if not show_hidden:
            if node.name[0] == '.':
                continue
        for _ in range(level):
            print('|   ', end='')
        print('+-- ', end='')
        if node.is_dir():
            print(node.name)
            printDirContents(node, level+1)
        else:
            print(node.name)

    for _ in range(level):
        print('|   ', end='')
    print()

if __name__ == '__main__':
    pytree()
