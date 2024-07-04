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

- Documentation accessibility checking.
- Documentation FAQ in contributing guidelines.

### Fixed

- Template documentation in light of accessibility issues of some features (namely, mkdocs-material annotations and task lists, and mkdocs-jupyter codeblock highlighting).

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
