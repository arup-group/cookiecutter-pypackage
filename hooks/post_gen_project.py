#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(filepath: Path | str):
    assert (PROJECT_DIRECTORY / filepath).exists()
    (PROJECT_DIRECTORY / filepath).unlink()


def remove_dir(dirpath: Path | str):
    (PROJECT_DIRECTORY / dirpath).rmdir()


if __name__ == "__main__":
    for file_to_delete in PROJECT_DIRECTORY.rglob(".ignore"):
        file_to_delete.unlink()

    if "{{ cookiecutter.create_author_file|lower }}" == "n":
        remove_file("AUTHORS")

    if "{{ cookiecutter.command_line_interface|lower }}" == "n":
        for file in [
            Path("{{ cookiecutter.module_name }}", "cli.py"),
            Path("tests", "test_cli.py"),
            Path("docs", "api", "cli.md"),
        ]:
            remove_file(file)

    if "{{ cookiecutter.create_jupyter_notebook_directory|lower }}" == "n":
        notebook_dir = Path("examples")
        for hidden_file in (PROJECT_DIRECTORY / notebook_dir).glob(".*"):
            hidden_file.unlink()
        remove_file(notebook_dir / "1_intro_to_{{cookiecutter.module_name}}.ipynb")
        remove_dir(notebook_dir)

    if "{{ cookiecutter.upload_conda_package|lower }}" == "n":
        recipe_dir = Path("conda.recipe")
        remove_file(recipe_dir / "meta.yaml")
        remove_dir(recipe_dir)

    if (
        "{{ cookiecutter.upload_conda_package|lower }}" == "n"
        and "{{ cookiecutter.upload_pypi_package|lower }}" == "n"
    ):
        workflow_dir = Path(".github") / "workflows"
        remove_file(workflow_dir / "pre-release.yml")

    if "{{ cookiecutter.create_docker_file|lower }}" == "n":
        for file in [".dockerignore", "Dockerfile"]:
            remove_file(file)

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")
