import os
import sys
from pathlib import Path


def cli(args):
    if len(args) == 1:
        print("Usage: python 05-cli.py <command>")
        return
    if len(args) != 3:
        print("Invalid number of arguments")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print(f"File {origen} does not exist")
        return

    os.rename(str(origen), str(args[2]))


cli(sys.argv)
