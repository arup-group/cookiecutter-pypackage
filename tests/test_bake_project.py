import datetime
import importlib
from pathlib import Path

import pytest
from click.testing import CliRunner


@pytest.fixture
def install_baked(bash):
    def _install_baked(dirpath: Path):
        bash.send(f"pip install --dry-run '{dirpath.as_posix()}'")

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
    assert "python_boilerplate" in found_toplevel_files
    assert "mkdocs.yml" in found_toplevel_files
    assert "tests" in found_toplevel_files


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
    assert (
        len(
            (result.project_path / "docs" / "overrides" / "main.html")
            .read_text()
            .strip()
            .split("\n")
        )
        == 1
    )


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
def test_bake_selecting_license(cookies, license, target_string):
    result = cookies.bake(extra_context={"open_source_license": license})
    assert target_string in (result.project_path / "LICENSE").read_text()


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
    assert (result.project_path / result.project_path.stem).exists()
    cli_file = result.project_path / result.project_path.stem / "cli.py"
    assert not cli_file.exists()

    setup_path = result.project_path / "pyproject.toml"
    assert "[project.scripts]" not in setup_path.read_text()


def test_bake_with_console_script_files(cookies):
    result = cookies.bake(extra_context={"command_line_interface": "y"})
    cli_file = result.project_path / result.project_path.stem / "cli.py"
    assert cli_file.exists()

    assert "[project.scripts]" in (result.project_path / "pyproject.toml").read_text()


def test_bake_with_console_script_cli(cookies):
    context = {"command_line_interface": "y"}
    result = cookies.bake(extra_context=context)
    package_name = result.project_path.stem
    module_path = result.project_path / package_name / "cli.py"
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
