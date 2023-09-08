# Tutorial

!!! note
    Did you find any of these instructions confusing? [Edit this file] and submit a pull request with your improvements!

[Edit this file]: https://github.com/arup-group/cookiecutter-pypackage/blob/main/docs/tutorial.md

To start with, you will need a [GitHub account](https://github.com/).
If you are an Arup employee, you should sign up to the Arup [GitHub group](https://github.arup.com/signup).

If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at [GitHub Help](https://help.github.com/).

## Step 1: Install Cookiecutter

First, you need to create and activate a conda/[mamba](https://mamba.readthedocs.io/en/latest/index.html) environment for using cookiecutter.
Use your favorite method, or create an environment like this:

``` bash
    mamba create -n cookiecutter cookiecutter
```

Activate your environment:

``` bash
    mamba activate cookiecutter
```

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

=== "Slim"

    ``` bash
        cookiecutter gh:arup-group/cookiecutter-pypackage
    ```

=== "Long-form"

    ``` bash
        cookiecutter https://github.com/arup-group/cookiecutter-pypackage.git
    ```

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


## Step 3: Create a GitHub Repository

Go to your GitHub account and create a new repository named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter.

You will find one folder named after the ``[project_slug]``.
Change directory into this folder, and then setup git to use your GitHub repo and upload the code:

```bash
    cd mypackage
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:HOST/mypackage.git
    git push -u origin main
```

Where `HOST` and `mypackage` are adjusted to the host group/user for your repository and the package name, respectively.

!!! note

    If you are uploading directly to an `arup-group` repository, use `arup-group` for `HOST`.


## Step 4: Define requirements

As well as writing the package source code, documentation, and tests, you will need to define the packages on which your project depends.
You can find an empty requirements file for you to complete in your new project folder: `requirements/base.txt`.

## Step 5: Create a development environment for your project

To install the necessary packages to develop your Python package, follow the instructions given in the new project's README / online documentation (https://HOST.github.io/mypackage, where `HOST` is the name of the owner of the repository on GitHub, e.g. `myusername` or `arup-group`).

## Step 6: Tweak the generated project files to meet your specific needs / preferences

Although we recommend you stick with the default setup provided by the template, there are a few files you may like to tweak / things you'll want to add.
This list is not exhaustive, but gives you an idea of where to look.

1. **Changing how continuous integration (CI) works**.
The configuration files in `.github/workflows` are based on the [PAM](https://github.com/arup-group/pam) package workflows.
They will run different levels of tests when pushing new commits and when opening pull requests.
You may want to change some of this configuration, e.g., the python versions that tests are run on or whether to notify a slack channel when CI fails/succeeds.

2. **Adding [repository secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository) for use in CI**.
To upload your package to an AWS S3 bucket you will need the secrets `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_CODE_BUCKET` available in your repository.
You also need secrets for uploading to Anaconda and initiating the Slack notification bot.
You can find all the secrets you need for different actions in the City Modelling Lab [actions repository](https://github.com/arup-group/actions-city-modelling-lab).

3. **Adding logos**.
The `resources` directory includes a logo subdirectory that you can add any branding for your package.
E.g., `resources/logos/title.png` will be shown at the top of the README, or you can add a [favicon](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/#favicon) and then link it to your documentation.

4. **Update linting strictness**.
We use [ruff](https://beta.ruff.rs/docs/) to ensure high code quality.
However, it checks only for a subset of possible issues with your code.
This is due to existing projects being very difficult to update to meet strict rules.
If you are starting a project from scratch, you may like to add more rules for it to check from its [extensive list](https://beta.ruff.rs/docs/rules/).

## Having problems?

__Is something not working?__

[:material-bug: Report a bug](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=BUG-REPORT.yml "Report a bug in the template by creating an issue and a reproduction"){ .md-button }

__Missing information in our docs?__

[:material-file-document: Report a docs issue](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=DOCS.yml "Report missing information or potential inconsistencies in our documentation"){ .md-button }

__Want to submit an idea?__

[:material-lightbulb-on: Request a change](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=FEATURE-REQUEST.yml "Propose a change or feature request or suggest an improvement"){ .md-button }

__Have a question or need help?__

[:material-chat-question: Ask a question](https://github.com/arup-group/cookiecutter-pypackage/discussions "Ask questions on our discussion board and get in touch with our community"){ .md-button }