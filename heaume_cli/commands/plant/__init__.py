"""The main file of the plant module"""
import click
import pendulum

from .ls import ls
from .status import status


@click.group()
def plant():
    """
    Heaume is a CLI that gives information about my home.

    Use 'heaume' to start
    """


plant.add_command(status)
plant.add_command(ls)
