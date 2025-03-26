# Arup Cookiecutter Python Package Template

>[!CAUTION]
>This project is now in maintenance mode.
>See the [Copier Python Package template](https://github.com/arup-group/pypackage-template) repository for the latest template.

[![Daily CI Build](https://github.com/arup-group/cookiecutter-pypackage/actions/workflows/daily-scheduled-ci.yml/badge.svg)](https://github.com/arup-group/cookiecutter-pypackage/actions/workflows/daily-scheduled-ci.yml)
[![Documentation](https://github.com/arup-group/cookiecutter-pypackage/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://arup-group.github.io/cookiecutter-pypackage)

[Cookiecutter] template for an Arup Python package.

This template is based on [@audreyfeldroy's original cookiecutter template](https://github.com/audreyfeldroy/cookiecutter-pypackage).
It has been updated to use latest Python Package best practices and to align with [Arup's City Modelling Lab Python projects](https://github.com/search?q=topic%3Acml+org%3Aarup-group&type=repositories).

## Features

- Testing setup with [pytest].
- Markdown based documentation, using [mkdocs], ready for generation with [GitHub pages].
- Project metadata and plugin configuration specified in a `pyproject.toml` file, according to the [latest standards].
- Auto-release to your private [conda] channel when you create a new release on GitHub (optional).
- Command line interface using [click] (optional).

[Cookiecutter]: https://github.com/cookiecutter/cookiecutter
[pytest]: https://docs.pytest.org
[mkdocs]: https://pypi.org/project/mkdocs/
[GitHub pages]: https://pages.github.com
[conda]: https://anaconda.org
[click]: https://click.palletsprojects.com
[latest standards]: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html

## Quickstart

To be able to keep your project up-tp-date as changes are made to the template, we recommend you use [Cruft], which is fully compatible with Cookiecutter.
First, install the latest version of Cruft if you haven't installed it yet.

``` bash
conda create -n cookiecutter cruft
conda activate cookiecutter
```

Generate a local Python package project in a directory of your choice (change `my-repositories` to the relevant location on your device):

``` bash
cd my-repositories
cruft create https://github.com/arup-group/cookiecutter-pypackage
```

[cruft]: https://cruft.github.io/cruft/

Then:

- Add the packages you will need for your project and their versions to `requirements/base.txt`.
- initialise your project as a git repository and link it to an online repository.

For more details, see the [tutorial](https://arup-group.github.io/cookiecutter-pypackage/latest/tutorial).

### Keeping your project up-to-date

We may make changes to this template that you want to pull into your project after you have created it.
Cruft allows you to do this, and one of your project's CI workflows will verify whether there are new template updates that you might like to merge in.

To check if there are updates:
``` bash
cruft check
```

To apply updates:
``` bash
cruft update
```

## Not Exactly What You Want?

Don't worry, you have options:

### Other Arup Cookiecutter Templates

There are currently no other Arup cookiecutter templates.

### Other Cookiecutter Templates

You can find a list of other Python project templates on the parent template repository: [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

### Fork This / Create Your Own

If you have differences in your preferred setup, you can fork this to create your own version.
Or you create your own; it doesn't strictly have to be a fork.

- Once you have your own version working, add it to the [Other Arup Cookiecutter Templates](#other-arup-cookiecutter-templates) list above with a brief description.
- It's up to you whether or not to rename your fork/own version. Do whatever you think sounds good.

### Or Submit a Pull Request

We also accept pull requests on this repository, if they're small!
