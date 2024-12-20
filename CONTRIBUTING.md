# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Issues

__Is something not working?__

[:material-bug: Report a bug](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=BUG-REPORT.yml "Report a bug in the template by creating an issue and a reproduction"){ .md-button }

__Missing information in our docs?__

[:material-file-document: Report a docs issue](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=DOCS.yml "Report missing information or potential inconsistencies in our documentation"){ .md-button }

__Want to submit an idea?__

[:material-lightbulb-on: Request a change](https://github.com/arup-group/cookiecutter-pypackage/issues/new?template=FEATURE-REQUEST.yml "Propose a change or feature request or suggest an improvement"){ .md-button }

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement a fix for it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

Cookiecutter PyPackage could always use more documentation, whether as part of the official docs, in docstrings, or even on the web in blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an [issue](https://github.com/arup-group/cookiecutter-pypackage/issues) or [start a discussion](https://github.com/arup-group/cookiecutter-pypackage/discussions).

If you are proposing a new feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.

## Setting up and working in a development environment

Ready to contribute? Here's how to set up `cookiecutter-pypackage` for local development.
Please note this documentation assumes you already have `conda` and `Git` installed and ready to go.

1. Fork the `cookiecutter-pypackage` repo on GitHub.

1. Clone your fork locally in a directory of your choice (i.e., change `path/to/repositories`):

   ``` shell
   cd path/to/repositories
   git clone git@github.com:YOUR_GITHUB_USERNAME/cookiecutter-pypackage.git
   ```

1. Assuming you have conda installed, you can create a new environment for your local
   development by typing:

   ``` shell
   conda create -c conda-forge -n cookiecutter-pypackage-dev --file requirements/dev.txt
   conda activate cookiecutter-pypackage-dev
   pip install --no-deps -e .
   ```

1. Install `pre-commit`, which will ensure your changes are properly formatted when you commit your code (or install extension to run Ruff and Black on save in your IDE):

   ``` shell
   pre-commit install
   ```

1. Create a branch for local development:

   ``` shell
   git checkout -b name-of-your-bugfix-or-feature
   ```

1. Make your changes! If your contribution is a bug fix or new feature, you may want to add a test to the existing test suite. See [Add a New Test](#add-a-new-test) below for details.

1. When you're done making changes on this new branch, run the tests:

   ``` shell
   pytest
   ```

1. Commit your changes and push your branch to GitHub:

   ``` shell
   git add .
   git commit -m "Your detailed description of your changes."
   git push origin name-of-your-bugfix-or-feature
   ```

1. Submit a pull request through the GitHub website.

### Pull Request (PR) Guidelines

Before you submit a PR, check that it meets these guidelines:

1. The changelog has been updated.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in README.md.

3. The PR should work for Python 3.10 - 3.12 (inclusive).
   Continuous integration tests will run in your PR and will fail if your changes break anything.

### Add to the template
Cookiecutter templates use [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating syntax.
For example, `{{ cookiecutter.module_name }}` -> `python_boilerplate` on running cookiecutter.
You can get a good feel for this by looking at the current implementation.

The GitHub CI workflows also use the `{{}}` syntax, requiring anything that should be left behind after cookiecutter works its magic to be wrapped in {% raw %} and {% endraw %} commands.

If you want to add an empty directory, you should add a `.ignore` file into it (e.g., see `resources/logos`).
This will ensure that cruft actually builds the directories.
In a post-generation hook, this `.ignore` file will be deleted and you will be left with the empty directory.

### Add a New Test

When fixing a bug or adding features, it's good practice to add a test to demonstrate your fix or new feature behaves as expected.
These tests should focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

1. Add the new test to `tests/test_bake_project.py`.
   Focus your test on the specific bug or a small part of the new feature.

1. If you have already made changes to the code, stash your changes and confirm all your changes were stashed:

   ``` shell
   git stash
   git stash list
   ```

1. Run your test and confirm that your test fails.
   If your test does not fail, rewrite the test until it fails on the original code:

   ``` shell
   pytest
   ```

1. Proceed work on your bug fix or new feature or restore your changes.
   To restore your stashed changes and confirm their restoration:

   ``` shell
   git stash pop
   git stash list
   ```

1. Rerun your test and confirm that your test passes.
   If it passes, congratulations!
