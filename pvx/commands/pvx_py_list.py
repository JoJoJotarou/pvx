import click

from tools.rich_pvx_console import console
from handler.py import pyHandler
import commands.py_help as help
from env import PVX_PYTHON_INSTALLATION_PATH


@click.command("list")
def cli():
    """A list of installed Python versions."""
    installed, installed_broken = pyHandler.list(PVX_PYTHON_INSTALLATION_PATH)
    if len(installed) > 0:
        console.print("Installed versions:\n")
        for _i in installed:
            console.print("   " + _i, pvx_emoji=False)
    if len(installed_broken) > 0:
        console.text("Broken Versions, Try reinstall:\n").help(help.py_install).print()
        for _ib in installed_broken:
            console.print("   " + _ib, pvx_emoji=False)

    if len(installed) == 0 and len(installed_broken) == 0:
        console.text("Nothing found ~, Try installing one:").help(
            help.py_install
        ).print()
