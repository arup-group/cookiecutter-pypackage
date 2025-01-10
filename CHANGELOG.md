<!---
Changelog headings can be any of:

Added: for new features.
Changed: for changes in existing functionality.
Deprecated: for soon-to-be removed features.
Removed: for now removed features.
Fixed: for any bug fixes.
Security: in case of vulnerabilities.
-->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] - TBC

### Added

- Human-readable prompts when baking a project (#56).
- EditorConfig file within template (#50).
- Documentation accessibility checking (#41).
- Documentation FAQ in contributing guidelines (#41).

### Fixed

- Missing Ruff formatting step in pre-commit config (#51).
- Template documentation in light of accessibility issues of some features (namely, mkdocs-material annotations and task lists, and mkdocs-jupyter codeblock highlighting) (#41).
- Triggering of CI linting and codecov upload for internal (i.e. not open-source) projects (#44).

### Changed

- Recommend `conda` instead of `mamba` for project creation and package installation (#53).
- Docs CI run on PR to main or on main, with different jobs run in each case (#33).
- Docs/PR CI jobs do not trigger on github workflow changes except their own definition files (#32).
- Package test parallelisation set to automatically select the number of threads based on those available (#36).
- Move to exclusively using `ruff` for code formatting and linting; update to `ruff` version 0.6 (#43).
- Cookiecutter config set to have no license for the repository (i.e. internal IP) by default.
- Make upload and build of Docker image on AWS optional (#42).

## [v0.2.0] - 09-01-2024

### Fixed

- Only run AWS upload job if secrets are defined.

### Added

- Upload to PyPI option.

### Changed

- Delete conda recipe if upload to conda is not desired.
- `index_package` cookiecutter parameter split into `upload_conda_package` and `upload_pypi_package`.
- Uploading to Anaconda/PyPI defaults to "n".
- Documentation split into separate pages for setting up and updating projects.

## [v0.1.0] - 05-01-2024

These initial changes are all relative to the [original cookiecutter PyPackage repository](https://github.com/audreyfeldroy/cookiecutter-pypackage), of which this is a fork.
The list is not exhaustive as many changes have been made.

### Fixed

### Added

- GitHub actions that rely on [City Modelling Lab reusable actions](https://github.com/arup-group/actions-city-modelling-lab).
- Schema for Cookiecutter input argument config (in `cookiecutter.json`) + tests added to CI to validate the config and the schema itself.
- Pre-commit hooks and pre-commit CI
- Templates for different types of GitHub issues.
- Cookiecutter contributing guidelines and changelog.
- Dockerfile to generate basic Docker image from project.
- Memory profiling test template.
- Option to include recipe to build project with `conda`, ready to trigger the appropriate reusable actions to have it built and uploaded to an Anaconda channel (e.g. `city-modelling-lab`).
- Option to have a Jupyter Notebook directory (under `examples`) which will be automatically linted, formatted, tested, and rendered in the documentation.

### Changed

- Documentation based on Markdown and MKDocs instead of ReStructured text and Sphinx (for improved readability and simpler configuration).
- Python project config moved from `setup.py` to `pyproject.toml`.
- Differentiating between repository name (for github), package name (for indexing online), and module name (for importing in python).
This extends the original use of `project_name` and `project_slug`, the latter being difficult to understand.

### Removed

- Use of Travis CI.
- Use of Tox.
- Upload to PyPi (with a plan to reintroduce this).
- Possibility to use Argparse for CLI (i.e., Click is now the only option).
