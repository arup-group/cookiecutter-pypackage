"""Hooks to run before baking the project from the template."""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_REGEX, module_name):
    print(
        f"ERROR: The package name ({module_name}) is not a valid Python module name. Please do not use a - and use _ instead"
    )

    # Exit to cancel project
    sys.exit(1)
