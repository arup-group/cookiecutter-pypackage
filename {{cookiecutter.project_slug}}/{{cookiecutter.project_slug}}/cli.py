"""Console script for {{cookiecutter.project_slug}}."""

import sys
import click


@click.command()
def cli(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo(
        "Replace this message by putting your code into " "{{cookiecutter.project_slug}}.cli.cli"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
