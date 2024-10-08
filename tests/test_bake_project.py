import datetime
import importlib
from pathlib import Path
from subprocess import PIPE, STDOUT, Popen

import pytest
from click.testing import CliRunner


@pytest.fixture
def install_baked():
    def _install_baked(dirpath: Path):
        pop = Popen(["pip", "install", "--dry-run", dirpath.as_posix()], stderr=STDOUT, stdout=PIPE)
        pop.wait()
        assert pop.returncode == 0

    return _install_baked


@pytest.fixture
def default_bake(cookies):
    result = cookies.bake()
    return result


def test_year_compute_in_license_file(default_bake):
    license_file_path = default_bake.project_path / "LICENSE"
    now = datetime.datetime.now()
    assert str(now.year) in license_file_path.read_text()


def test_bake_with_defaults(default_bake, install_baked):
    assert default_bake.project_path.is_dir()
    assert default_bake.exit_code == 0
    assert default_bake.exception is None
    install_baked(default_bake.project_path)


def test_bake_with_defaults_top_level_files(default_bake):
    found_toplevel_files = [i.name for i in default_bake.project_path.iterdir()]
    assert "pyproject.toml" in found_toplevel_files
    assert "src" in found_toplevel_files
    assert "mkdocs.yml" in found_toplevel_files
    assert "tests" in found_toplevel_files
    assert list(i.stem for i in (default_bake.project_path / "src").iterdir()) == [
        "python_boilerplate"
    ]


def test_bake_with_defaults_src_code_files(default_bake):
    found_src_code_files = [
        i.name for i in (default_bake.project_path / "src" / "python_boilerplate").iterdir()
    ]
    assert set(found_src_code_files) == {"py.typed", "__init__.py", "core.py", "cli.py"}


def test_bake_withspecialchars_and_run_tests(cookies, install_baked):
    """Ensure that a `full_name` with double quotes does not break setup.py"""
    result = cookies.bake(extra_context={"full_name": 'name "quote" name'})
    install_baked(result.project_path)


def test_bake_with_apostrophe_and_run_tests(cookies, install_baked):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    result = cookies.bake(extra_context={"full_name": "O'connor"})
    install_baked(result.project_path)


@pytest.mark.parametrize("project_title", ["Foo Bar", "Foo-Bar"])
def test_bake_with_slugify_project_title(cookies, install_baked, project_title):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    result = cookies.bake(extra_context={"project_title": project_title})
    assert result.project_path.stem == "foo_bar"
    install_baked(result.project_path)


def test_bake_explicit_repository_name(cookies, install_baked):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    result = cookies.bake(extra_context={"project_title": "Foo's-Bar", "repository_name": "foobar"})
    assert result.project_path.stem == "foobar"
    install_baked(result.project_path)


def test_bake_without_author_file(cookies):
    result = cookies.bake(extra_context={"create_author_file": "n"})

    found_toplevel_files = [i.name for i in result.project_path.iterdir()]
    assert "AUTHORS" not in found_toplevel_files


def test_bake_without_docker_file(cookies):
    result = cookies.bake(extra_context={"create_docker_file": "n"})

    found_toplevel_files = [i.name for i in result.project_path.iterdir()]
    assert "Dockerfile" not in found_toplevel_files
    assert ".dockerignore" not in found_toplevel_files


def test_bake_without_jupyter_notebooks(cookies):
    result = cookies.bake(extra_context={"create_jupyter_notebook_directory": "n"})

    found_toplevel_files = [i.name for i in result.project_path.iterdir()]
    assert "examples" not in found_toplevel_files
    assert "nbmake" not in (result.project_path / "pyproject.toml").read_text()
    assert "Examples" not in (result.project_path / "mkdocs.yml").read_text()
    assert "jupyter" not in (result.project_path / "mkdocs.yml").read_text()
    assert "nbmake" not in (result.project_path / "requirements" / "dev.txt").read_text()
    assert "nbmake" not in (result.project_path / "docs" / "contributing.md").read_text()
    assert "kernel" not in (result.project_path / "docs" / "contributing.md").read_text()
    assert "kernel" not in (result.project_path / "docs" / "contributing.md").read_text()

    html_override = (result.project_path / "docs" / "overrides" / "main.html").read_text().strip()
    assert '{% extends "base.html" %}' in html_override
    assert "page.nb_url" not in html_override


def test_bake_without_conda(cookies):
    result = cookies.bake(extra_context={"upload_conda_package": "n", "upload_pypi_package": "y"})

    found_toplevel_files = [i.name for i in result.project_path.iterdir()]
    assert "conda.recipe" not in found_toplevel_files


@pytest.mark.parametrize("destination", ["conda", "pypi"])
def test_bake_without_indexing_one(cookies, destination):
    other_option = set(["conda", "pypi"]).difference([destination]).pop()
    result = cookies.bake(
        extra_context={f"upload_{destination}_package": "n", f"upload_{other_option}_package": "y"}
    )

    for workflow in ["pre-release", "release"]:
        github_workflow = (
            result.project_path / ".github" / "workflows" / f"{workflow}.yml"
        ).read_text()
        assert f"{destination}-" not in github_workflow


def test_bake_without_indexing_all(cookies):
    result = cookies.bake(extra_context={"upload_pypi_package": "n", "upload_conda_package": "n"})

    workflows = [i.name for i in (result.project_path / ".github" / "workflows").iterdir()]
    assert "pre-release.yml" not in workflows


@pytest.mark.parametrize(
    ["license", "target_string"],
    [
        ("MIT license", "MIT "),
        (
            "BSD license",
            "Redistributions of source code must retain the above copyright notice, this",
        ),
        ("ISC license", "ISC License"),
        ("Apache Software License 2.0", "Licensed under the Apache License, Version 2.0"),
        ("GNU General Public License v3", "GNU GENERAL PUBLIC LICENSE"),
    ],
)
@pytest.mark.parametrize(
    ["owner", "expected_copyright"], [("arup-group", "Arup"), ("Foo Bar", "Foo Bar")]
)
def test_bake_selecting_license(cookies, license, target_string, owner, expected_copyright):
    result = cookies.bake(extra_context={"open_source_license": license, "repository_owner": owner})
    assert target_string in (result.project_path / "LICENSE").read_text()
    assert f"Copyright (c) {str(datetime.datetime.now().year)} {expected_copyright}"


@pytest.mark.parametrize(
    ["license", "target_string"],
    [
        ("MIT license", "MIT"),
        ("BSD license", "BSD"),
        ("ISC license", "ISCL"),
        ("Apache Software License 2.0", "Apache"),
        ("GNU General Public License v3", "GPL"),
    ],
)
def test_bake_selecting_license_in_toml(cookies, license, target_string):
    result = cookies.bake(extra_context={"open_source_license": license})
    assert target_string in (result.project_path / "pyproject.toml").read_text()


def test_bake_not_open_source(cookies):
    result = cookies.bake(extra_context={"open_source_license": "Not open source"})

    found_toplevel_files = [i.name for i in result.project_path.iterdir()]
    assert "pyproject.toml" in found_toplevel_files
    assert "LICENSE" not in found_toplevel_files
    assert "License" not in (result.project_path / "README.md").read_text()


def test_bake_with_no_console_script(cookies):
    result = cookies.bake(extra_context={"command_line_interface": "n"})
    assert (result.project_path / "src" / result.project_path.stem).exists()
    cli_file = result.project_path / result.project_path.stem / "cli.py"
    assert not cli_file.exists()

    setup_path = result.project_path / "pyproject.toml"
    assert "[project.scripts]" not in setup_path.read_text()


def test_bake_with_console_script_files(cookies):
    result = cookies.bake(extra_context={"command_line_interface": "y"})
    cli_file = result.project_path / "src" / result.project_path.stem / "cli.py"
    assert cli_file.exists()

    assert "[project.scripts]" in (result.project_path / "pyproject.toml").read_text()


def test_bake_with_console_script_cli(cookies):
    context = {"command_line_interface": "y"}
    result = cookies.bake(extra_context=context)
    package_name = result.project_path.stem
    module_path = result.project_path / "src" / package_name / "cli.py"
    module_name = ".".join([package_name, "cli"])
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    cli = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cli)
    runner = CliRunner()
    noarg_result = runner.invoke(cli.cli)
    assert noarg_result.exit_code == 0
    noarg_output = " ".join(["Replace this message by putting your code into", package_name])
    assert noarg_output in noarg_result.output
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message" in help_result.output


def test_bake_no_a11y_default(default_bake):
    assert (
        "docs-accessibility"
        not in (default_bake.project_path / ".github" / "workflows" / "docs.yml").read_text()
    )
    assert (
        "### Ensuring accessibility"
        not in (default_bake.project_path / "docs" / "contributing.md").read_text()
    )


def test_bake_a11y(cookies):
    result = cookies.bake(extra_context={"check_docs_accessibility_in_CI": "y"})
    assert (
        "docs-accessibility"
        in (result.project_path / ".github" / "workflows" / "docs.yml").read_text()
    )
    assert (
        "### Ensuring accessibility"
        in (result.project_path / "docs" / "contributing.md").read_text()
    )

def test_aws_missing_in_default(default_bake):
    assert not any(
        i in (default_bake.project_path / ".github" / "workflows" / "commit-ci.yml").read_text()
        for i in ["aws-pre-check", "aws-upload"]
    )


def test_activate_aws_upload(cookies):
    result = cookies.bake(extra_context={"upload_aws_image": "y"})

    assert all(
        i in (result.project_path / ".github" / "workflows" / "commit-ci.yml").read_text()
        for i in ["aws-pre-check", "aws-upload"]
    )
