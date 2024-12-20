# Tutorial

!!! note
    Did you find any of these instructions confusing? [Edit this file] and submit a pull request with your improvements!

[Edit this file]: https://github.com/arup-group/cookiecutter-pypackage/blob/main/docs/tutorial.md

To start with, you will need a [GitHub account](https://github.com/).
If you are an Arup employee, you should sign up to the Arup [GitHub group](https://github.arup.com/signup).

If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at [GitHub Help](https://help.github.com/).

## Setting up your project

!!! note annotate

    We will refer to project names, directories, github accounts, etc. in this tutorial.
    You will be using different ones for your project, with the possible exception of `arup-group` as the `repository_owner`.
    For reference, here's the [configuration values][configuration-values] we will use that you will have the option to set when creating your project with cruft:

    - `github_username`: "ovearup"
    - `repository_owner`: "arup-group"
    - `project_title`: "Python Boilerplate"
    - `repository_name`: "python-boilerplate"
    - `package_name`: "cml-python-boilerplate" (1)
    - `module_name`: "python_boilerplate" (2)

    Here are some of the assumptions we will make about your local system, which you will need to change as necessary:

    - You have [mamba](https://mamba.readthedocs.io/en/latest/index.html) installed (conda/micromamba also work)
    - You store your projects on your device at `~/Repos` (Windows: `C:\\Users\yourusername\Repos`)

1.  The package name needs to be *globally* unique, i.e., not available on [conda-forge](https://anaconda.org/conda-forge) or on [PyPI](https://pypi.org/).
This is why it could look different to `repository_name` and `module_name`.
Search for your preferred package name before setting it here.
In the City Modelling Lab, we use the `cml-` prefix if we need to make our package name unique.
2.  Repositories tend to use `-` between words while modules **must** have `_` between words as this is the name you will use to import your module in Python: `import python_boilerplate`.

### Step 1: Install Cruft

First, you need to create and activate a conda/[mamba](https://mamba.readthedocs.io/en/latest/index.html) environment for using Cruft (a Cookiecutter-compatible tool which allows for project updating).
Use your favorite method, or create an environment like this:

=== "With mamba"
    ``` bash
    mamba create -n cookiecutter cruft
    ```
    Activate your environment:

    ``` bash
    mamba activate cookiecutter
    ```

=== "With pip"
    ``` bash
    pip install -U cruft
    ```

### Step 2: Generate Your Package

Now it's time to generate your Python package.

Use cruft, pointing it at the cookiecutter-pypackage repository:

``` bash
cd ~/Repos # (1)!
cruft create https://github.com/arup-group/cookiecutter-pypackage.git
```

1.  Change this directory name to match where you store GitHub repositories on your device.

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.
The following steps are based on using the default values.

Once complete, you will find the `python-boilerplate` directory.
Change directory into this folder:

```bash
cd python-boilerplate # (1)!
```

1.  Change this directory name based on the name you gave in `repository_name`.

!!! tip

    If you are generating a project which will be hosted in `arup-group`, it will default to `internal`.
    This is why we set the `project_visibility` parameter to `internal` by default.

    The parameters `upload_conda_package` and `upload_pip_package` default to `n` (i.e. no upload of packages), but you can set these to `y` to upload `internal` projects the Arup package index (<https://packages.arup.com/>) so long as you make a service-now request to allow access to the `packages` self-hosted runner for your repository.

    You will need to wait until the project is made public (with a suitable open source license) before you allow uploads of your package to PyPI or an Anaconda channel.
    When you're ready to take the leap to a public repository, you can [update your project input parameters][changing-input-parameters-after-project-generation] to set the project visibility to `public`.
    At this point, you will need to add PyPI/Anaconda upload tokens to your repository "secrets", as [described below](#step-7-tweak-the-generated-project-files-to-meet-your-specific-needs--preferences).

### Step 3: Create a GitHub Repository

Go to the GitHub page for `[repository_owner]`, e.g. `https://github.com/arup-group` or `https://github.com/ovearup`, and create a new repository with `[repository_name]` (`python-boilerplate`).

Do not add anything to your account: no `README`, no `LICENSE`, no `.gitignore`.
Everything will be added when you push your newly generated package.

Once you have your repository created, go back to your command line where you are inside your newly created local project, then upload that code:

```bash
git init .
git add .
git commit -m "Initial skeleton."
git branch -M main
git remote add origin git@github.com:arup-group/python-boilerplate.git # (1)!
git push -u origin main
```

1.  Change `python-boilerplate` to match the name you have gave in `repository-name`.

Where `arup-group` and `python-boilerplate` are adjusted to the host group/user for your repository and the package name, respectively.

### Step 4: Enable GitHub pages for your documentation

Once you have uploaded your project to your repository, return to the repository and [set up GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) to host your documentation.
You should choose the `gh-pages` branch (this will only appear a few minutes after you push your first commit) under the `Branch` dropdown.

!!! note

    If `master` is the default name for your primary project branch, the documentation will not build automatically.
    You should ensure you have [renamed your primary branch to `main`](https://github.com/github/renaming).

!!! warning

    If the repository is in your own user account (e.g., `overarup`), it must be a public repository to be able to host documentation using github pages.
    If the repository is in `arup-group`, then it can be `internal` (the default) and still host documentation using github pages.

### Step 5: Define requirements

As well as writing the package source code, documentation, and tests, you will need to define the packages on which your project depends.
You can find an _almost_ empty requirements file for you to complete in your new project folder: `requirements/base.txt`.
It cannot be empty, otherwise mamba might complain.
You can update this as you go along and need new packages in your project.

### Step 6: Create a development environment for your project

To install the necessary packages to develop your Python package, follow the instructions automatically generated in your new project's README / online documentation (e.g., https://arup-group.github.io/python-boilerplate).

!!! note
    As you update the requirements that [you define as dependencies](#step-5-define-requirements), you should bulldoze your install and recreate it.
    E.g., if you create your environment using mamba/conda:

    ```bash
    mamba create -n python-boilerplate -c conda-forge --file requirements/base.txt --file requirements/dev.txt
    ```

    You should run this exact same command after updating `requirements/base.txt` and say yes to overriding the existing `python-boilerplate` environment.
    This is a much better way of managing your python environments than adding the dependencies ad-hoc using `mamba install ...`.

### Step 7: Tweak the generated project files to meet your specific needs / preferences

Although we recommend you stick with the default setup provided by the template, there are a few files you may like to tweak / things you'll want to add.
This list is not exhaustive, but gives you an idea of where to look.

1. **Changing how continuous integration (CI) works**.
The configuration files in `.github/workflows` are based on the [PAM](https://github.com/arup-group/pam) package workflows and rely on the City Modelling Lab's [reusable workflows](https://github.com/arup-group/actions-city-modelling-lab).
They will run different levels of tests when pushing new commits and when opening pull requests.
You may want to change some of this configuration, e.g., the python versions that tests are run on or whether to (1) notify a slack channel when CI fails/succeeds and (2) attempt to upload the package to AWS (if the `upload_aws_image` configuration option is active).

2. **Adding [repository secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) for use in CI**.
To upload your package to Anaconda (`upload_conda_package`), you will need an [API token](https://server-docs.anaconda.com/en/latest/user/auth_token.html) saved as the `ANACONDA_TOKEN` repository secret.
To upload to an AWS S3 bucket (`upload_aws_image`) you will need the secrets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_CODE_BUCKET` available in your repository.
You also need secrets for initiating the Slack notification bot and uploading to an AWS S3 bucket (+ possibly some AWS terraforming).
You can find all the secrets you need for different actions in the City Modelling Lab [reusable workflow repository](https://github.com/arup-group/actions-city-modelling-lab).

!!! note:
    Some secrets should be stored in [GitHub environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment).
    Namely, releasing packages to public packages indexes should be in `pre-release` (for `.github/workflows/pre-release.yml` job secrets) and `release` (for `.github/workflows/release.yml` job secrets) environments.
    We recommend you then place protection rules on those environments to only allow maintainers to release the workflow jobs.

3. **Adding logos**.
The `resources` directory includes a logo subdirectory that you can add any branding for your package.
E.g., `resources/logos/title.png` will be shown at the top of the README, or you can add a [favicon](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#favicon) and then link it to your documentation.

4. **Updating linting strictness**.
We use [ruff](https://beta.ruff.rs/docs/) to ensure high code quality.
However, it checks only for a subset of possible issues with your code.
This is due to existing projects being very difficult to update to meet strict rules.
If you are starting a project from scratch, you may like to add more rules for it to check from its [extensive list](https://beta.ruff.rs/docs/rules/).

5. **limiting conda build architectures**.
By default, the conda package (if you choose to have one built) will build one package for all architectures (i.e., windows, linux, macos, ...).
Usually, your dependencies will be aligned with this: they will also be installable on any architecture.
However, there are times when you might have a dependency that can not be installed on e.g., Windows.
If that is the case, be sure to dive into `conda.recipe/meta.yaml` and change some lines in `build` following the comments there.

## Having problems?

__Is something not working?__

[:material-bug: Report a bug](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=BUG-REPORT.yml "Report a bug in the template by creating an issue and a reproduction"){ .md-button }

__Missing information in our docs?__

[:material-file-document: Report a docs issue](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=DOCS.yml "Report missing information or potential inconsistencies in our documentation"){ .md-button }

__Want to submit an idea?__

[:material-lightbulb-on: Request a change](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=FEATURE-REQUEST.yml "Propose a change or feature request or suggest an improvement"){ .md-button }

__Have a question or need help?__

[:material-chat-question: Ask a question](https://github.com/arup-group/cookiecutter-pypackage/discussions "Ask questions on our discussion board and get in touch with our community"){ .md-button }
