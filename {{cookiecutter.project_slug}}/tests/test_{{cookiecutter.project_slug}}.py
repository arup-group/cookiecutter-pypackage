#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import pytest
{%- if cookiecutter.command_line_interface|lower == "y" %}
from click.testing import CliRunner
{%- endif %}

{% if cookiecutter.command_line_interface|lower == "y" -%}
from {{ cookiecutter.project_slug }} import cli, {{ cookiecutter.project_slug }}
{%- else %}
from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}
{%- endif %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/arup-group/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    print({{ cookiecutter.project_slug }}.__file__)
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


{% if cookiecutter.command_line_interface|lower == "y" -%}
def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}.cli.cli" in result.output
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{%- endif %}
