# Arup Python Package Template

[![Daily CI Build](https://github.com/arup-group/pypackage-template/actions/workflows/daily-scheduled-ci.yml/badge.svg)](https://github.com/arup-group/pypackage-template/actions/workflows/daily-scheduled-ci.yml)
[![Documentation](https://github.com/arup-group/pypackage-template/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://arup-group.github.io/pypackage-template)

[Copier] template for an Arup Python package.

This template was originally based on [@audreyfeldroy's original cookiecutter template](https://github.com/audreyfeldroy/cookiecutter-pypackage).
It has been updated to use latest Python Package best practices, to align with [Arup's City Modelling Lab Python projects](https://github.com/search?q=topic%3Acml+org%3Aarup-group&type=repositories), and to use the [Copier] template manager.

## Features

- Testing setup with [pytest].
- Markdown based documentation, using [mkdocs], ready for generation with [GitHub pages].
- Project metadata and plugin configuration specified in a `pyproject.toml` file, according to the [latest standards].
- Auto-release to your private [conda] channel when you create a new release on GitHub (optional).
- Command line interface using [click] (optional).

[Copier]: https://copier.readthedocs.io
[pytest]: https://docs.pytest.org
[mkdocs]: https://pypi.org/project/mkdocs/
[GitHub pages]: https://pages.github.com
[conda]: https://anaconda.org
[click]: https://click.palletsprojects.com
[latest standards]: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

## Quickstart

First, install the latest version of Copier:

``` bash
conda create -n copier-env copier
conda activate copier-env
```

Generate a local Python package project in a directory of your choice (change `my-repositories` to the relevant location on your device):

``` bash
cd my-repositories
copier copy https://github.com/arup-group/pypackage-template .
```

Then:

- Add the packages you will need for your project and their versions to `requirements/base.txt`.
  You can remove `zipp` and the commented lines in the process.
- initialise your project as a git repository and link it to an online repository.

For more details, see the [tutorial](https://arup-group.github.io/pypackage-template/latest/tutorial).

### Keeping your project up-to-date

We may make changes to this template that you want to pull into your project after you have created it.
Copier allows you to do this, and one of your project's CI workflows will verify whether there are new template updates that you might like to merge in.

To check if there are updates:

``` sh
copier update --pretend
```

To apply updates:

``` sh
copier update
```

## Not Exactly What You Want?

Don't worry, you have options:

### Other Arup templates

- [ESOP project template](https://github.com/arup-group/esop-template).
  This is a template for starting an [ESOP](https://github.com/arup-group/esop-py) project.
- [ESOP datashop product template](https://github.com/arup-group/esop-datashop).
  This is a template for contributing an open API data product which will be hosted on DataBricks.

### Other Templates

- [Calliope project snakemake module template](https://github.com/calliope-project/data-module-template)

[Cookiecutter](https://cookiecutter.readthedocs.io/) is another template engine, for which there are a number of Python project templates linked on the parent template repository: [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

### Fork This / Create Your Own

If you have differences in your preferred setup, you can fork this to create your own version.
Or you create your own; it doesn't strictly have to be a fork.

- Once you have your own version working, add it to the ["other Arup templates"](#other-arup-templates) list above with a brief description.
- It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

### Or Submit a Pull Request

We also accept pull requests on this repository, if they're small!
