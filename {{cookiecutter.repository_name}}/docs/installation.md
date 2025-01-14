
# Installation

## Setting up a user environment

{% if cookiecutter.project_visibility == "internal" and (cookiecutter.upload_conda_package == "y"  or cookiecutter.upload_pip_package == "y") -%}
!!! note
    You must be on the Arup network to install {{ cookiecutter.module_name }}, either by connecting in an office or via the Arup VPN.
{% endif -%}

As a `{{ cookiecutter.module_name }}` user, it is easiest to install using the [conda](https://docs.conda.io/en/latest/) package manager, as follows:

1. Install conda with the [miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file#download) executable for your operating system.
Arup users on Windows can install `miniforge` from the Arup software shop by downloading "VS Code for Python".
1. Open the command line (or the VSCode "integrated terminal" in Windows).
{%- if cookiecutter.upload_conda_package == "y" %}
1. Create the {{ cookiecutter.repository_name }} conda environment: `conda create -n {{ cookiecutter.repository_name }} -c conda-forge -c {{ cookiecutter.conda_channel }} {{ cookiecutter.package_name }}`
1. Activate the {{ cookiecutter.repository_name }} conda environment: `conda activate {{ cookiecutter.repository_name }}`
{%- elif cookiecutter.upload_pip_package == "y" %}
1. Create a {{ cookiecutter.repository_name }} conda environment: `conda create -n {{ cookiecutter.repository_name }} -c conda-forge python`
1. Activate the {{ cookiecutter.repository_name }} conda environment: `conda activate {{ cookiecutter.repository_name }}`
{%- if cookiecutter.project_visibility == "internal" %}
1. Install the {{ cookiecutter.package_name }} package into the environment: `pip install https://packages.arup.com/{{ cookiecutter.package_name }}.tar.gz`
{%- else %}
1. Install the {{ cookiecutter.package_name }} package into the environment: `pip install {{ cookiecutter.package_name }}`
{%- endif %}
{%- else %}
1. Download (a.k.a., clone) the {{ cookiecutter.repository_name }} repository: `git clone git@github.com:{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}.git`
1. Change into the `{{ cookiecutter.repository_name }}` directory: `cd {{ cookiecutter.repository_name }}`
1. Create the {{ cookiecutter.repository_name }} conda environment: `conda create -n {{ cookiecutter.repository_name }} -c conda-forge -c city-modelling-lab --file requirements/base.txt`
1. Activate the {{ cookiecutter.repository_name }} conda environment: `conda activate {{ cookiecutter.repository_name }}`
1. Install the {{ cookiecutter.package_name }} package into the environment, ignoring dependencies (we have dealt with those when creating the conda environment): `pip install --no-deps .`
{% endif %}

All together:

--8<-- "README.md:docs-install-user"

!!! tip
    If you are an Arup user and are having difficulties with creating the `conda` environment, it may be due to *SSL certificates*.
    You'll know that this is the case because there will be mention of "SSL" in the error trace.
    Search `SSL Certificates` on the Arup internal Sharepoint to find instructions on adding the certificates for `conda`.
    Windows users who have installed "VS Code for Python" from the software shop should have all the relevant certificates in place, but you will need to follow the instructions given on the SharePoint troubleshooting page if you want to run the command from in a Windows Subsystem for Linux (WSL) session.

{%- if cookiecutter.create_jupyter_notebook_directory|lower == "y" %}

### Running the example notebooks

If you have followed the non-developer installation instructions above, you will need to install `jupyter` into your `{{ cookiecutter.repository_name }}` environment to run the [example notebooks](https://github.com/{{ cookiecutter.repository_owner }}/{{ cookiecutter.repository_name }}/tree/main/examples):

``` shell
conda install -n {{ cookiecutter.repository_name }} jupyter
```

With Jupyter installed, it's easiest to then add the environment as a jupyter kernel:

``` shell
conda activate {{ cookiecutter.repository_name }}
ipython kernel install --user --name={{ cookiecutter.repository_name }}
jupyter notebook
```

### Choosing a different environment name

If you would like to use a different name to `{{ cookiecutter.repository_name }}` for your conda environment, the installation becomes (where `[my-env-name]` is your preferred name for the environment):

``` shell
conda create -n [my-env-name] -c conda-forge --file requirements/base.txt
conda activate [my-env-name]
ipython kernel install --user --name=[my-env-name]
```
{%- endif %}

## Setting up a development environment

The install instructions are slightly different to create a development environment compared to a user environment:

--8<-- "README.md:docs-install-dev"

For more detailed installation instructions specific to developing the {{ cookiecutter.module_name }} codebase, see our [development documentation][setting-up-a-development-environment].
