"""Console script for {{cookiecutter.module_name}}."""

import click


@click.version_option(package_name="{{cookiecutter.package_name}}")
@click.command()
def cli(args=None):
    """Console script for {{cookiecutter.module_name}}."""
    click.echo(
        "Replace this message by putting your code into {{cookiecutter.module_name}}.cli.cli"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
