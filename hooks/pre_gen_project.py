"""Hooks to run before baking the project from the template."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.module_name }}"
is_internal = "{{ cookiecutter.project_visibility }}" == "internal"

if not re.match(MODULE_REGEX, module_name):
    print(
        f"ERROR: The package name ({module_name}) is not a valid Python module name. Please do not use a `-` and use `_` instead"
    )

    # Exit to cancel project
    sys.exit(1)

if not is_internal and "{{ cookiecutter.open_source_license }}" == "Not open source":
    print("ERROR: 'public' projects must have a license.")

    # Exit to cancel project
    sys.exit(1)

if (
    is_internal
    and "{{ cookiecutter.conda_channel }}".rstrip("/") != "https://packages.arup.com/conda"
    and "{{ cookiecutter.upload_conda_package }}" == "y"
):
    print(
        "ERROR: 'internal' projects must set the `conda_channel` to: https://packages.arup.com/conda."
    )

    # Exit to cancel project
    sys.exit(1)

if is_internal and (
    "{{ cookiecutter.upload_conda_package }}" == "y"
    or "{{ cookiecutter.upload_pip_package }}" == "y"
):
    print(
        "NOTE: You must request access to the `packages` GitHub self-hosted runner for 'internal' projects being uploaded to https://packages.arup.com/conda."
    )
