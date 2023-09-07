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

## [Unreleased]

These initial changes are all relative to the [original cookiecutter PyPackage repository](https://github.com/audreyfeldroy/cookiecutter-pypackage), of which this is a fork.
The list is not exhaustive as many changes have been made.

### Fixed

### Added

- GitHub actions that rely on [City Modelling Lab reusable actions](https://github.com/arup-group/actions-city-modelling-lab).
- Schema for Cookiecutter input argument config (in `cookiecutter.json`) + tests added to CI to validate the config and the schema itself.
- Templates for different types of GitHub issues.
- Cookiecutter contributing guidelines and changelog.
- Dockerfile to generate basic Docker image from project.
- memory profiling test template.
### Changed

- Documentation based on Markdown and MKDocs instead of ReStructured text and Sphinx (for improved readability and simpler configuration).
- Python project config moved from `setup.py` to `pyproject.toml`.

### Removed

- Use of Travis CI.
- Use of Tox.
- Upload to PyPi (with a plan to reintroduce this).
- Possibility to use Argparse for CLI (i.e., Click is now the only option).
