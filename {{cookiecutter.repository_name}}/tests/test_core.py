"""Tests for `{{ cookiecutter.module_name }}` package."""

from {{ cookiecutter.module_name }} import core


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    print(core.__file__)
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
