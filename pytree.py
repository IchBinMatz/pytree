from pathlib import Path
import click 
ITEM = "+--"
SEPERATOR = "|   "

@click.command()
@click.option(
    "--hidden/--no-hidden",
    default=False,
    show_default=True,
    help="show hidden files and folders",
)
@click.argument(
    "directory", type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
def pytree(directory: Path, hidden: bool):
    """ converts the input directory into a readable filetree"""
    d = Path(directory)
    printDirContents(d, show_hidden=hidden)

def printDirContents(directory: Path, level=0, show_hidden=False):
    """ reads the directory recursivly and prints all the files and subdirectorys"""
    if show_hidden:
        children = directory.glob("./*")
    else:
        children = directory.glob("./[!.]*")
    dirs = []
    files = []
    for node in children:
        if node.is_dir():
            dirs.append(node)
        if node.is_file():
            files.append(node)
    for d in sorted(dirs):
        printSeperator(level)
        printItem(d.name)
        printDirContents(d, level + 1)
    for f in sorted(files):
        printSeperator(level)
        printItem(f.name)

    printSeperator(level, end='\n')

def printSeperator(level : int, end=""):
    for _ in range(level):
        print(SEPERATOR, end=end)

def printItem(name: str):
    print(f"{ITEM} {name}")


if __name__ == "__main__":
    pytree()
