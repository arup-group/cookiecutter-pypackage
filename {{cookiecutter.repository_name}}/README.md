<!--- the "--8<--" html comments define what part of the README to add to the index page of the documentation -->
<!--- --8<-- [start:docs] -->
![{{ cookiecutter.module_name }}](resources/logos/title.png)

# {{ cookiecutter.project_title }} ({{ cookiecutter.module_name }})

{% if cookiecutter.project_visibility == 'internal' -%}
<!--- --8<-- [end:docs] -->

{% endif -%}
[![Daily CI Build](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/actions/workflows/daily-scheduled-ci.yml/badge.svg)](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/actions/workflows/daily-scheduled-ci.yml)
[![Documentation](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://{{ cookiecutter.repository_owner }}.github.io/{{ cookiecutter.repository_name }})

{% if cookiecutter.project_visibility == 'public' -%}
<!--- --8<-- [end:docs] -->

{% endif -%}
## Documentation

For more detailed instructions, see our [documentation](https://{{ cookiecutter.repository_owner }}.github.io/{{ cookiecutter.repository_name }}/latest).

## Installation

To install {{ cookiecutter.module_name }}
{%- if cookiecutter.package_name != cookiecutter.module_name %}
 (indexed online as {{ cookiecutter.package_name }})
{%- endif -%}
, we recommend using the [conda](https://docs.conda.io/en/latest/) package manager, accessible from the terminal by installing [miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#download).
Arup users on Windows can install `miniforge` from the Arup software shop by downloading "VS Code for Python" and then access `conda` from the VSCode integrated terminal.

### As a user

<!--- --8<-- [start:docs-install-user] -->

``` shell
{% if cookiecutter.upload_conda_package == "y" -%}
conda create -n {{ cookiecutter.repository_name }} -c conda-forge -c {{ cookiecutter.conda_channel }} {{ cookiecutter.package_name }}
conda activate {{ cookiecutter.repository_name }}
{% elif cookiecutter.upload_pip_package == "y" %}
conda create -n {{ cookiecutter.repository_name }} -c conda-forge python
conda activate {{ cookiecutter.repository_name }}
{%- if cookiecutter.project_visibility == "internal" %}
pip install https://packages.arup.com/{{ cookiecutter.package_name }}.tar.gz
{%- else %}
pip install {{ cookiecutter.package_name }}
{%- endif %}
{% else %}
git clone git@github.com:{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}.git
cd {{ cookiecutter.repository_name }}
conda create -n {{ cookiecutter.repository_name }} -c conda-forge --file requirements/base.txt
conda activate {{ cookiecutter.repository_name }}
pip install --no-deps -e .
{%- endif %}
```

<!--- --8<-- [end:docs-install-user] -->

### As a developer

<!--- --8<-- [start:docs-install-dev] -->

``` shell
git clone git@github.com:{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}.git
cd {{ cookiecutter.repository_name }}
conda create -n {{ cookiecutter.repository_name }} -c conda-forge --file requirements/base.txt --file requirements/dev.txt
conda activate {{ cookiecutter.repository_name }}
pip install --no-deps -e .
```

<!--- --8<-- [end:docs-install-dev] -->

For more detailed instructions, see our [documentation](https://{{ cookiecutter.repository_owner }}.github.io/{{ cookiecutter.repository_name }}/latest/installation/).

## Contributing

There are many ways to contribute to {{ cookiecutter.repository_name }}.
Before making contributions to the {{ cookiecutter.module_name }} source code, see our contribution guidelines and follow the [development install instructions](#as-a-developer).

If you plan to make changes to the code then please make regular use of the following tools to verify the codebase while you work:

- `pre-commit`: run `pre-commit install` in your command line to load inbuilt checks that will run every time you commit your changes.
  The checks are: 1. check no large files have been staged, 2. lint python files for major errors, 3. format python files to conform with the [pep8 standard](https://peps.python.org/pep-0008/).
  You can also run these checks yourself at any time to ensure staged changes are clean by simple calling `pre-commit`.
- `pytest` - run the unit test suite and check test coverage.
- `pytest -p memray -m "high_mem" --no-cov` (not available on Windows) - after installing memray (`conda install memray pytest-memray`), test that memory and time performance does not exceed benchmarks.

For more information, see our [documentation](https://{{ cookiecutter.repository_owner }}.github.io/{{ cookiecutter.repository_name }}/latest/contributing/).

## Building the documentation

If you are unable to access the online documentation, you can build the documentation locally.
First, [install a development environment of {{ cookiecutter.repository_name }}](https://{{ cookiecutter.repository_owner }}.github.io/{{ cookiecutter.repository_name }}/latest/contributing/coding/), then deploy the documentation using [MkDocs](https://www.mkdocs.org/):

``` shell
mkdocs serve
```

Then you can view the documentation in a browser at <http://localhost:8000/>.

## License

Copyright (c) {% now 'local', '%Y' %} {% if cookiecutter.repository_owner == "arup-group" %}Arup{% elif cookiecutter.create_author_file == "y" %}{{ cookiecutter.package_name }} developers & contributors listed in AUTHORS.md{% else %}{{ cookiecutter.full_name }}{% endif %}.

{%- if cookiecutter.open_source_license == "Not open source" %}
This repository is not open source.
You will need explicit permission from the repository owner to redistribute or make any modifications to this code.
{%- else %}
Licensed under the {{ cookiecutter.open_source_license }}.
{%- endif %}

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [arup-group/cookiecutter-pypackage](https://github.com/arup-group/cookiecutter-pypackage) project template.
