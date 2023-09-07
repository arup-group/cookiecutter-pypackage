# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

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

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

## Setting up and working in a development environment

Ready to contribute? Here's how to set up `cookiecutter-pypackage` for local development.
Please note this documentation assumes you already have `mamba` and `Git` installed and ready to go.

1. Fork the `cookiecutter-pypackage` repo on GitHub.

2. Clone your fork locally in a directory of your choice (i.e., change `path/to/repositories`):

``` bash
cd path/to/repositories
git clone git@github.com:YOUR_GITHUB_USERNAME/cookiecutter-pypackage.git
```

3. Assuming you have mamba installed, you can create a new environment for your local
   development by typing:

``` bash
mamba create -c conda-forge -n cookiecutter-pypackage-dev --file requirements/dev.txt
mamba activate cookiecutter-pypackage-dev
pip install --no-deps -e .
```

4. Install `pre-commit`, which will ensure your changes are properly formatted when you commit your code (or install extension to run Ruff and Black on save in your IDE):

``` bash
pre-commit install
```

4. Create a branch for local development:

``` bash
git checkout -b name-of-your-bugfix-or-feature
```

4. Make your changes! If your contribution is a bug fix or new feature, you may want to add a test to the existing test suite. See [Add a New Test](#add-a-new-test) below for details.

5. When you're done making changes on this new branch, run the tests:

```bash
pytest
```

9. Commit your changes and push your branch to GitHub:

```bash
git add .
git commit -m "Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

10. Submit a pull request through the GitHub website.


### Pull Request (PR) Guidelines

Before you submit a PR, check that it meets these guidelines:

1. The changelog has been updated.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add the feature to the list in README.md.

3. The PR should work for Python 3.9 - 3.11 (inclusive).
   Continuous integration tests will run in your PR and will fail if your changes break anything.

### Add a New Test

When fixing a bug or adding features, it's good practice to add a test to demonstrate your fix or new feature behaves as expected.
These tests should focus on one tiny bit of functionality and prove changes are correct.

To write and run your new test, follow these steps:

1. Add the new test to `tests/test_bake_project.py`.
   Focus your test on the specific bug or a small part of the new feature.

2. If you have already made changes to the code, stash your changes and confirm all your changes were stashed:
```bash
git stash
git stash list
```

3. Run your test and confirm that your test fails.
   If your test does not fail, rewrite the test until it fails on the original code:
```bash
pytest
```

5. Proceed work on your bug fix or new feature or restore your changes.
   To restore your stashed changes and confirm their restoration:
```bash
git stash pop
git stash list
```

6. Rerun your test and confirm that your test passes.
   If it passes, congratulations!

