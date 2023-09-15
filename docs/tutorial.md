# Tutorial

!!! note
    Did you find any of these instructions confusing? [Edit this file] and submit a pull request with your improvements!

[Edit this file]: https://github.com/arup-group/cookiecutter-pypackage/blob/main/docs/tutorial.md

To start with, you will need a [GitHub account](https://github.com/).
If you are an Arup employee, you should sign up to the Arup [GitHub group](https://github.arup.com/signup).

If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at [GitHub Help](https://help.github.com/).

## Setting up your project

!!! note

    We will refer to project names, directories, github accounts, etc. in this tutorial.
    You will be using different ones for your project, with the possible exception of `arup-group` as the `repository_org`.
    For reference, here's the [configuration values][#configuration-values] we will use that you will have the option to set when creating your project with cruft:
    - `github_username`: "ovearup"
    - `repository_org`: "arup-group"
    - `project_title`: "Python Boilerplate"
    - `repository_name`: "python-boilerplate"
    - `package_name`: "python_boilerplate"
    Here are some of the assumptions we will make about your local system, which you will need to change as necessary:
    - You have [mamba](https://mamba.readthedocs.io/en/latest/index.html) installed (conda/micromamba also work)
    - You store your projects on your device at `~/Repos` (Windows: `C:\\Users\yourusername\Repos`)

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
    cd ~/Repos
    cruft create https://github.com/arup-group/cookiecutter-pypackage.git
```

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.
The following steps are based on using the default values.

Once complete, you will find the `python-boilerplate` directory.
Change directory into this folder: `cd python-boilerplate`

### Step 3: Create a GitHub Repository

Go to the GitHub page for `[repository_org]`, e.g. `https://github.com/arup-group` or `https://github.com/ovearup`, and create a new repository with `[repository_name]` (`python-boilerplate`).

Do not add anything to your account: no `README`, no `LICENSE`, no `.gitignore`.
Everything will be added when you push your newly generated package.

!!! note

    If the repository is in your own user account (e.g., `overarup`), you may benefit from making it a public repository to be able to host documentation using github pages.

Once you have your repository created, go back to your command line where you are inside your newly created local project, then upload that code:

```bash
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:arup-group/python-boilerplate.git
    git push -u origin main
```

Where `arup-group` and `python-boilerplate` are adjusted to the host group/user for your repository and the package name, respectively.

Once you have uploaded your project to your repository, return to the repository and [set up GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) to host your documentation.
You should choose the `gh-pages` branch (this will only appear a few minutes after you push your first commit) under the `Branch` dropdown.

!!! note

    If `master` is the default name for your primary project branch, the documentation will not build automatically.
    You should ensure you have [renamed your primary branch to `main`](https://github.com/github/renaming).

### Step 4: Define requirements

As well as writing the package source code, documentation, and tests, you will need to define the packages on which your project depends.
You can find an _almost_ empty requirements file for you to complete in your new project folder: `requirements/base.txt`.
It cannot be empty, otherwise mamba might complain.
You can keep update this as you go along and need new packages in your project.

### Step 5: Create a development environment for your project

To install the necessary packages to develop your Python package, follow the instructions automatically generated in your new project's README / online documentation (e.g., https://arup-group.github.io/python-boilerplate).

!!! note
    As you update the requirements that [you define as dependencies][#step-4-define-requirements], you should bulldoze your install and recreate it.
    E.g., if you create your environment using mamba/conda:
    ```bash
    mamba create -n python-boilerplate -c conda-forge --file requirements/base.txt --file requirements/dev.txt
    ```
    You should run this exact same command after updating `requirements/base.txt` and say yes to overriding the existing `python-boilerplate` environment.
    This is a much better way of managing your python environments than adding the dependencies ad-hoc using `mamba install ...`.

### Step 6: Tweak the generated project files to meet your specific needs / preferences

Although we recommend you stick with the default setup provided by the template, there are a few files you may like to tweak / things you'll want to add.
This list is not exhaustive, but gives you an idea of where to look.

1. **Changing how continuous integration (CI) works**.
The configuration files in `.github/workflows` are based on the [PAM](https://github.com/arup-group/pam) package workflows and rely on the City Modelling Lab's [reusable workflows](https://github.com/arup-group/actions-city-modelling-lab).
They will run different levels of tests when pushing new commits and when opening pull requests.
You may want to change some of this configuration, e.g., the python versions that tests are run on or whether to (1) notify a slack channel when CI fails/succeeds and (2) attempt to upload the package to AWS.

2. **Adding [repository secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) for use in CI**.
To upload your package to Anaconda, you will need an [API token](https://server-docs.anaconda.com/en/latest/user/auth_token.html) saved as the `ANACONDA_TOKEN` repository secret.
To upload to an AWS S3 bucket you will need the secrets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_CODE_BUCKET` available in your repository.
You also need secrets for initiating the Slack notification bot and uploading to an AWS S3 bucket (+ possibly some AWS terraforming).

You can find all the secrets you need for different actions in the City Modelling Lab [reusable workflow repository](https://github.com/arup-group/actions-city-modelling-lab).

3. **Adding logos**.
The `resources` directory includes a logo subdirectory that you can add any branding for your package.
E.g., `resources/logos/title.png` will be shown at the top of the README, or you can add a [favicon](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#favicon) and then link it to your documentation.

4. **Updating linting strictness**.
We use [ruff](https://beta.ruff.rs/docs/) to ensure high code quality.
However, it checks only for a subset of possible issues with your code.
This is due to existing projects being very difficult to update to meet strict rules.
If you are starting a project from scratch, you may like to add more rules for it to check from its [extensive list](https://beta.ruff.rs/docs/rules/).

## Keeping your project up-to-date

We may make changes to this template that you want to pull into your project after you have created it.
Cruft allows you to do this, and one of your project's CI workflows will verify whether there are new template updates that you might like to merge in.

Check if there are updates:
``` bash
    cruft check
```

View the diff between your project and the most up-to-date template:
``` bash
    cruft diff
```

Apply any updates that exist:

``` bash
    cruft update
```

!!! note
    There is a limit to how well cruft can apply an update.
    More likely than not, it will produce a lot of `.rej` files explaining what updates it tried to implement, but failed to merge in.
    You will need to go through each of these manually and make the changes in the corresponding source code file.

## Changing inputs after project generation

You can change your mind on *some* of the input variables you gave when initialising the project and use `cruft` to update them.

The following variables are suitable for updating:

- full_name
- email
- github_username
- repository_org
- project_title
- repository_name
- package_name
- project_short_description
- conda_channel
- version
- open_source_license

Even when changing one of these values, be aware that you will need to apply some manual changes based on `.rej` files that cruft will generate.

## Having problems?

__Is something not working?__

[:material-bug: Report a bug](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=BUG-REPORT.yml "Report a bug in the template by creating an issue and a reproduction"){ .md-button }

__Missing information in our docs?__

[:material-file-document: Report a docs issue](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=DOCS.yml "Report missing information or potential inconsistencies in our documentation"){ .md-button }

__Want to submit an idea?__

[:material-lightbulb-on: Request a change](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=FEATURE-REQUEST.yml "Propose a change or feature request or suggest an improvement"){ .md-button }

__Have a question or need help?__

[:material-chat-question: Ask a question](https://github.com/arup-group/cookiecutter-pypackage/discussions "Ask questions on our discussion board and get in touch with our community"){ .md-button }