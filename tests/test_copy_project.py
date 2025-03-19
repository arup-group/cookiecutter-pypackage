import datetime
import importlib
from pathlib import Path
from subprocess import PIPE, STDOUT, Popen

import copier
import pytest
from click.testing import CliRunner


@pytest.fixture
def install_copied():
    def _install_copied(dirpath: Path):
        pop = Popen(["pip", "install", "--dry-run", dirpath.as_posix()], stderr=STDOUT, stdout=PIPE)
        pop.wait()
        assert pop.returncode == 0

    return _install_copied


@pytest.fixture(scope="session")
def default_copy(tmp_path_factory):
    repo_dir = Path(__file__).parent.parent
    tmp_path = tmp_path_factory.mktemp("project")
    with copier.Worker(
        src_path=str(repo_dir), dst_path=tmp_path, vcs_ref="HEAD", defaults=True
    ) as worker:
        worker.run_copy()
    return tmp_path / "python_boilerplate"


@pytest.fixture
def non_default_copy(tmp_path):
    def _non_default_copy(answers: dict, expected_proj_path: str = "python_boilerplate"):
        repo_dir = Path(__file__).parent.parent
        with copier.Worker(
            src_path=str(repo_dir), dst_path=tmp_path, vcs_ref="HEAD", data=answers, defaults=True
        ) as worker:
            worker.run_copy()
        return tmp_path / expected_proj_path

    return _non_default_copy


def test_year_compute_in_license_file(non_default_copy):
    dst_path = non_default_copy({"open_source_license": "MIT"})
    now = datetime.datetime.now()
    assert str(now.year) in (dst_path / "LICENSE").read_text()


def test_copy_with_defaults(default_copy, install_copied):
    assert default_copy.is_dir()
    install_copied(default_copy)


def test_copy_with_defaults_top_level_files(default_copy):
    found_toplevel_files = [i.name for i in default_copy.iterdir()]
    assert "pyproject.toml" in found_toplevel_files
    assert "src" in found_toplevel_files
    assert "mkdocs.yml" in found_toplevel_files
    assert "tests" in found_toplevel_files
    assert "python_boilerplate" in list(i.stem for i in (default_copy / "src").iterdir())


def test_copy_with_defaults_src_code_files(default_copy):
    found_src_code_files = [i.name for i in (default_copy / "src" / "python_boilerplate").iterdir()]
    assert set(found_src_code_files) == {"py.typed", "__init__.py", "core.py", "cli.py"}


def test_copy_withspecialchars_and_run_tests(non_default_copy, install_copied):
    """Ensure that a `full_name` with double quotes does not break setup.py"""
    dst_path = non_default_copy({"full_name": 'name "quote" name'})
    install_copied(dst_path)


def test_copy_with_apostrophe_and_run_tests(non_default_copy, install_copied):
    """Ensure that a `full_name` with apostrophes does not break setup.py"""
    dst_path = non_default_copy({"full_name": "O'connor"})
    install_copied(dst_path)


@pytest.mark.parametrize("project_title", ["Foo Bar", "Foo-Bar"])
def test_copy_with_slugify_project_title(non_default_copy, install_copied, project_title):
    """Ensure that project titles with spaces or dashes are slugified by default for the repo name."""
    dst_path = non_default_copy({"project_title": project_title}, "foo_bar")
    assert dst_path.stem == "foo_bar"
    install_copied(dst_path)


def test_copy_explicit_repository_name(non_default_copy, install_copied):
    """Ensure that a non-default repo name overrides the copier-generated default one."""
    dst_path = non_default_copy(
        {"project_title": "Foo's-Bar", "repository_name": "foobar"}, "foobar"
    )
    assert dst_path.stem == "foobar"
    install_copied(dst_path)


@pytest.mark.parametrize("create_author_file", [True, False])
def test_copy_with_or_without_author_file(non_default_copy, create_author_file):
    dst_path = non_default_copy({"create_author_file": create_author_file})

    found_toplevel_files = [i.name for i in dst_path.iterdir()]
    assert ("AUTHORS.md" in found_toplevel_files) is create_author_file
    assert (
        "When you contribute for the first time, ensure you add your name to the contributors list in `AUTHORS.md`!"
        in (dst_path / "CONTRIBUTING.md").read_text()
    ) is create_author_file


@pytest.mark.parametrize("license_name", ["MIT", "BSD", "Apache-2.0", "GPL-v3"])
@pytest.mark.parametrize(
    ["org_name", "copyright_name"], [("arup-group", "Arup"), ("foobar", "Ove Arup")]
)
def test_copy_license_without_author_file(non_default_copy, license_name, org_name, copyright_name):
    dst_path = non_default_copy({
        "create_author_file": "n",
        "open_source_license": license_name,
        "repository_owner": org_name,
    })

    for file in ["LICENSE", "README.md", "CONTRIBUTING.md"]:
        assert (
            f"Copyright (c) {datetime.datetime.now().year} {copyright_name}."
            in (dst_path / file).read_text()
        )


@pytest.mark.parametrize("license_name", ["MIT", "BSD", "Apache-2.0", "GPL-v3"])
@pytest.mark.parametrize("create_author_file", [True, False])  # should make no difference
def test_copy_license_with_author_file_and_arup_org(
    non_default_copy, license_name, create_author_file
):
    dst_path = non_default_copy({
        "create_author_file": create_author_file,
        "open_source_license": license_name,
        "repository_owner": "arup-group",
    })

    for file in ["LICENSE", "README.md", "CONTRIBUTING.md"]:
        assert (
            f"Copyright (c) {datetime.datetime.now().year} Arup." in (dst_path / file).read_text()
        )


@pytest.mark.parametrize("license_name", ["MIT", "BSD", "Apache-2.0", "GPL-v3"])
def test_copy_license_with_author_file(non_default_copy, license_name):
    dst_path = non_default_copy({
        "create_author_file": True,
        "open_source_license": license_name,
        "repository_owner": "foobar",
    })

    for file in ["LICENSE", "README.md", "CONTRIBUTING.md"]:
        assert (
            f"Copyright (c) {datetime.datetime.now().year} python_boilerplate developers & contributors listed in AUTHORS."
            in (dst_path / file).read_text()
        )


def test_copy_without_docker_file(non_default_copy):
    dst_path = non_default_copy({"create_docker_file": "n"})

    found_toplevel_files = [i.name for i in dst_path.iterdir()]
    assert "Dockerfile" not in found_toplevel_files
    assert ".dockerignore" not in found_toplevel_files


def test_copy_without_jupyter_notebooks(non_default_copy):
    dst_path = non_default_copy({"create_jupyter_notebook_directory": "n"})

    found_toplevel_files = [i.name for i in dst_path.iterdir()]
    assert "examples" not in found_toplevel_files
    assert "nbmake" not in (dst_path / "pyproject.toml").read_text()
    assert "Examples" not in (dst_path / "mkdocs.yml").read_text()
    assert "jupyter" not in (dst_path / "mkdocs.yml").read_text()
    assert "nbmake" not in (dst_path / "requirements" / "dev.txt").read_text()
    assert "nbmake" not in (dst_path / "docs" / "contributing.md").read_text()
    assert "kernel" not in (dst_path / "docs" / "contributing.md").read_text()
    assert "kernel" not in (dst_path / "docs" / "contributing.md").read_text()

    assert "main.html" not in (dst_path / "docs" / "overrides").glob("*")


def test_copy_without_conda(non_default_copy):
    dst_path = non_default_copy({"upload_conda_package": "n", "upload_pip_package": "y"})

    found_toplevel_files = [i.name for i in dst_path.iterdir()]
    assert "conda.recipe" not in found_toplevel_files


@pytest.mark.parametrize("destination", ["conda", "pip"])
def test_copy_without_indexing_one(non_default_copy, destination):
    other_option = set(["conda", "pip"]).difference([destination]).pop()
    dst_path = non_default_copy({
        f"upload_{destination}_package": "y",
        f"upload_{other_option}_package": "n",
    })

    for workflow in ["pre-release", "release"]:
        github_workflow = (dst_path / ".github" / "workflows" / f"{workflow}.yml").read_text()
        assert f"{destination}-" in github_workflow
        assert f"{other_option}-" not in github_workflow


def test_copy_without_indexing_all(non_default_copy):
    dst_path = non_default_copy({"upload_pip_package": "n", "upload_conda_package": "n"})

    workflows = [i.name for i in (dst_path / ".github" / "workflows").iterdir()]
    assert "pre-release.yml" not in workflows


@pytest.mark.parametrize(
    "extras",
    [
        {"upload_conda_package": "y"},
        {"upload_pip_package": "y"},
        {"upload_conda_package": "y", "upload_pip_package": "y"},
    ],
)
def test_copy_indexing_internal_destination(non_default_copy, extras):
    dst_path = non_default_copy({"conda_channel": "https://packages.arup.com/conda", **extras})

    for workflow in ["pre-release", "release"]:
        github_workflow = (dst_path / ".github" / "workflows" / f"{workflow}.yml").read_text()
        assert "destination: internal" in github_workflow
        assert "destination: public" not in github_workflow


@pytest.mark.parametrize(
    ["extras", "expected"],
    [
        (
            {"project_visibility": "internal"},
            "pip install https://packages.arup.com/python_boilerplate.tar.gz",
        ),
        (
            {"project_visibility": "public", "open_source_license": "MIT"},
            "pip install python_boilerplate",
        ),
    ],
)
def test_copy_indexing_internal_pip_destination(non_default_copy, extras, expected):
    dst_path = non_default_copy({"upload_pip_package": "y", **extras})

    for file in ["README.md", "docs/installation.md"]:
        install_instructions = (dst_path / file).read_text()

        assert expected in install_instructions


def test_copy_indexing_internal_fail_on_default_channel(non_default_copy):
    with pytest.raises(
        ValueError,
        match="Internal projects must set the `conda_channel` to: https://packages.arup.com/conda.",
    ):
        non_default_copy({"upload_conda_package": "y", "conda_channel": "foobar"})


@pytest.mark.parametrize(
    "extras",
    [
        {"upload_conda_package": "y"},
        {"upload_pip_package": "y"},
        {"upload_conda_package": "y", "upload_pip_package": "y"},
    ],
)
def test_copy_indexing_internal_destination_packages_warning(non_default_copy, capfd, extras):
    non_default_copy({"conda_channel": "https://packages.arup.com/conda", **extras})
    captured = capfd.readouterr()
    assert (
        "You must request access to the `packages` GitHub self-hosted runner for 'internal' projects"
        in captured.err
    )


def test_copy_public_and_no_license(non_default_copy):
    with pytest.raises(ValueError, match="'public' projects must have a license."):
        non_default_copy({"project_visibility": "public", "open_source_license": "not_open_source"})


@pytest.mark.parametrize(
    ["license", "target_string"],
    [
        ("MIT", "MIT "),
        ("BSD", "Redistributions of source code must retain the above copyright notice, this"),
        ("Apache-2.0", "Licensed under the Apache License, Version 2.0"),
        ("GPL-v3", "GNU GENERAL PUBLIC LICENSE"),
    ],
)
@pytest.mark.parametrize(
    ["owner", "expected_copyright"], [("arup-group", "Arup"), ("foo-bar", "Ove Arup")]
)
def test_copy_selecting_license(
    non_default_copy, license, target_string, owner, expected_copyright
):
    dst_path = non_default_copy({"open_source_license": license, "repository_owner": owner})
    assert target_string in (dst_path / "LICENSE").read_text()
    assert f"Copyright (c) {str(datetime.datetime.now().year)} {expected_copyright}"


@pytest.mark.parametrize(
    ["license", "target_string"],
    [("MIT", "MIT"), ("BSD", "BSD"), ("Apache-2.0", "Apache"), ("GPL-v3", "GPL")],
)
def test_copy_selecting_license_in_toml(non_default_copy, license, target_string):
    dst_path = non_default_copy({"open_source_license": license})
    assert target_string in (dst_path / "pyproject.toml").read_text()


def test_copy_not_open_source(non_default_copy):
    dst_path = non_default_copy({"open_source_license": "not_open_source"})

    found_toplevel_files = [i.name for i in dst_path.iterdir()]
    assert "pyproject.toml" in found_toplevel_files
    assert "LICENSE" not in found_toplevel_files


def test_copy_with_no_console_script(non_default_copy):
    dst_path = non_default_copy({"command_line_interface": "n"})
    assert (dst_path / "src" / dst_path.stem).exists()
    cli_file = dst_path / dst_path.stem / "cli.py"
    assert not cli_file.exists()

    setup_path = dst_path / "pyproject.toml"
    assert "[project.scripts]" not in setup_path.read_text()


def test_copy_with_console_script_files(non_default_copy):
    dst_path = non_default_copy({"command_line_interface": "y"})
    cli_file = dst_path / "src" / dst_path.stem / "cli.py"
    assert cli_file.exists()

    assert "[project.scripts]" in (dst_path / "pyproject.toml").read_text()


def test_copy_with_console_script_cli(non_default_copy):
    context = {"command_line_interface": "y"}
    dst_path = non_default_copy(context)
    package_name = dst_path.stem
    module_path = dst_path / "src" / package_name / "cli.py"
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


def test_copy_no_a11y_default(default_copy):
    assert (
        "docs-accessibility"
        not in (default_copy / ".github" / "workflows" / "docs.yml").read_text()
    )
    assert (
        "### Ensuring accessibility" not in (default_copy / "docs" / "contributing.md").read_text()
    )


def test_copy_a11y(non_default_copy):
    dst_path = non_default_copy({"check_docs_accessibility_in_CI": "y"})
    assert "docs-accessibility" in (dst_path / ".github" / "workflows" / "docs.yml").read_text()
    assert "### Ensuring accessibility" in (dst_path / "docs" / "contributing.md").read_text()


def test_aws_missing_in_default(default_copy):
    assert not any(
        i in (default_copy / ".github" / "workflows" / "commit-ci.yml").read_text()
        for i in ["aws-pre-check", "aws-upload"]
    )


def test_activate_aws_upload(non_default_copy):
    dst_path = non_default_copy({"upload_aws_image": "y"})

    assert all(
        i in (dst_path / ".github" / "workflows" / "commit-ci.yml").read_text()
        for i in ["aws-pre-check", "aws-upload"]
    )


def test_activate_aws_upload_message(non_default_copy, capfd):
    non_default_copy({"upload_aws_image": "y"})

    captured = capfd.readouterr()
    assert (
        "You must set the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_S3_CODE_BUCKET GitHub secrets using your AWS API tokens."
        in captured.err
    )
