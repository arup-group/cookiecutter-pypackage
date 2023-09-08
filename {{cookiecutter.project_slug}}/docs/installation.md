
# Installation

## Setting up a user environment

As a `{{ cookiecutter.project_slug }}` user, it is easiest to install using the [mamba](https://mamba.readthedocs.io/en/latest/index.html) package manager, as follows:


1. Install mamba with the [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) executable for your operating system.
2. Open the command line (or the "miniforge prompt" in Windows).
{% if cookiecutter.index_package == "conda" %}
3. mamba create -n {{ cookiecutter.project_slug }} -c conda-forge -c {{ cookiecutter.conda_channel }} {{ cookiecutter.project_slug }}
4. Activate the {{ cookiecutter.project_slug }} mamba environment: `mamba activate {{ cookiecutter.project_slug }}`
{% elif cookiecutter.index_package == "pypi" %}
1. mamba create -n {{ cookiecutter.project_slug }} -c conda-forge
3. Activate the {{ cookiecutter.project_slug }} mamba environment: `mamba activate {{ cookiecutter.project_slug }}`
4. Install the {{ cookiecutter.project_slug }} package: `pip install {{ cookiecutter.project_slug }}`
{% else %}
1. Install mamba with the [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) executable for your operating system.
2. Open the command line (or the "miniforge prompt" in Windows).
3. Download (a.k.a., clone) the {{ cookiecutter.project_slug }} repository: `git clone git@github.com:{{ cookiecutter.repository_org }}/{{ cookiecutter.project_slug }}.git`
4. Change into the `{{ cookiecutter.project_slug }}` directory: `cd {{ cookiecutter.project_slug }}`
5. Create the {{ cookiecutter.project_slug }} mamba environment: `mamba create -n {{ cookiecutter.project_slug }} -c conda-forge -c city-modelling-lab --file requirements/base.txt`
6. Activate the {{ cookiecutter.project_slug }} mamba environment: `mamba activate {{ cookiecutter.project_slug }}`
7. Install the {{ cookiecutter.project_slug }} package into the environment, ignoring dependencies (we have dealt with those when creating the mamba environment): `pip install --no-deps .`
{% endif %}

All together:

--8<-- "README.md:docs-install-user"

{%- if cookiecutter.create_jupyter_notebook_directory|lower == "y" %}
### Running the example notebooks
If you have followed the non-developer installation instructions above, you will need to install `jupyter` into your `{{ cookiecutter.project_slug }}` environment to run the [example notebooks](https://github.com/{{ cookiecutter.repository_org }}/{{ cookiecutter.project_slug }}/tree/main/examples):

``` shell
mamba install -n {{ cookiecutter.project_slug }} jupyter
```

With Jupyter installed, it's easiest to then add the environment as a jupyter kernel: 

``` shell
mamba activate {{ cookiecutter.project_slug }}
ipython kernel install --user --name={{ cookiecutter.project_slug }}
jupyter notebook
```

### Choosing a different environment name
If you would like to use a different name to `{{ cookiecutter.project_slug }}` for your mamba environment, the installation becomes (where `[my-env-name]` is your preferred name for the environment):

``` shell
mamba create -n [my-env-name] -c conda-forge --file requirements/base.txt
mamba activate [my-env-name]
ipython kernel install --user --name=[my-env-name]
```
{% endif -%}

## Setting up a development environment

The install instructions are slightly different to create a development environment compared to a user environment:

--8<-- "README.md:docs-install-dev"

For more detailed installation instructions specific to developing the {{ cookiecutter.project_slug }} codebase, see our [development documentation][setting-up-a-development-environment].
