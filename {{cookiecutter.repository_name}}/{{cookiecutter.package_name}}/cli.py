"""Console script for {{cookiecutter.package_name}}."""

import click


@click.command()
def cli(args=None):
    """Console script for {{cookiecutter.package_name}}."""
    click.echo(
        "Replace this message by putting your code into {{cookiecutter.package_name}}.cli.cli"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
