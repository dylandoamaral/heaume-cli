import click
import pendulum
from .status import status
from .ls import ls

@click.group()
def plant():
    """
    Heaume is a CLI that gives information about my home.

    Use 'heaume' to start
    """
    pass

plant.add_command(status)
plant.add_command(ls)
