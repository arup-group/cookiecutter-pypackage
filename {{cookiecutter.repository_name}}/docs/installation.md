
# Installation

## Setting up a user environment

As a `{{ cookiecutter.module_name }}` user, it is easiest to install using the [mamba](https://mamba.readthedocs.io/en/latest/index.html) package manager, as follows:

1. Install mamba with the [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) executable for your operating system.
2. Open the command line (or the "miniforge prompt" in Windows).
{% if cookiecutter.index_package == "conda" %}
3. Create the {{ cookiecutter.repository_name }} mamba environment: `mamba create -n {{ cookiecutter.repository_name }} -c conda-forge -c {{ cookiecutter.conda_channel }} {{ cookiecutter.repository_name }}`
4. Activate the {{ cookiecutter.repository_name }} mamba environment: `mamba activate {{ cookiecutter.repository_name }}`
{% else %}
1. Install mamba with the [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) executable for your operating system.
2. Open the command line (or the "miniforge prompt" in Windows).
3. Download (a.k.a., clone) the {{ cookiecutter.repository_name }} repository: `git clone git@github.com:{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}.git`
4. Change into the `{{ cookiecutter.repository_name }}` directory: `cd {{ cookiecutter.repository_name }}`
5. Create the {{ cookiecutter.repository_name }} mamba environment: `mamba create -n {{ cookiecutter.repository_name }} -c conda-forge -c city-modelling-lab --file requirements/base.txt`
6. Activate the {{ cookiecutter.repository_name }} mamba environment: `mamba activate {{ cookiecutter.repository_name }}`
7. Install the {{ cookiecutter.package_name }} package into the environment, ignoring dependencies (we have dealt with those when creating the mamba environment): `pip install --no-deps .`
{% endif %}

All together:

--8<-- "README.md:docs-install-user"

{%- if cookiecutter.create_jupyter_notebook_directory|lower == "y" %}
### Running the example notebooks
If you have followed the non-developer installation instructions above, you will need to install `jupyter` into your `{{ cookiecutter.repository_name }}` environment to run the [example notebooks](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/tree/main/examples):

``` shell
mamba install -n {{ cookiecutter.repository_name }} jupyter
```

With Jupyter installed, it's easiest to then add the environment as a jupyter kernel:

``` shell
mamba activate {{ cookiecutter.repository_name }}
ipython kernel install --user --name={{ cookiecutter.repository_name }}
jupyter notebook
```

### Choosing a different environment name
If you would like to use a different name to `{{ cookiecutter.repository_name }}` for your mamba environment, the installation becomes (where `[my-env-name]` is your preferred name for the environment):

``` shell
mamba create -n [my-env-name] -c conda-forge --file requirements/base.txt
mamba activate [my-env-name]
ipython kernel install --user --name=[my-env-name]
```
{%- endif %}

## Setting up a development environment

The install instructions are slightly different to create a development environment compared to a user environment:

--8<-- "README.md:docs-install-dev"

For more detailed installation instructions specific to developing the {{ cookiecutter.module_name }} codebase, see our [development documentation][setting-up-a-development-environment].
