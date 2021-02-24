"""The main file of the Heaume CLI"""
import click
import pendulum

from heaume_cli.commands.plant import plant


@click.group()
def heaume():
    """
    Heaume is a CLI that gives information about my home.

    Use 'heaume' to start
    """


heaume.add_command(plant)
heaume()
