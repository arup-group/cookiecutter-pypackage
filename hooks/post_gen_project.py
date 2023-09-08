#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(filepath: Path | str):
    assert (PROJECT_DIRECTORY / filepath).exists()
    (PROJECT_DIRECTORY / filepath).unlink()


def remove_dir(dirpath: Path | str):
    (PROJECT_DIRECTORY / dirpath).rmdir()


if __name__ == "__main__":
    if "{{ cookiecutter.create_author_file|lower }}" == "n":
        remove_file("AUTHORS")

    if "{{ cookiecutter.command_line_interface|lower }}" == "n":
        cli_file = Path() / "{{ cookiecutter.project_slug }}" / "cli.py"
        cli_docs = Path() / "docs" / "api" / "cli.md"
        remove_file(cli_file)
        remove_file(cli_docs)

    if "{{ cookiecutter.create_jupyter_notebook_directory|lower }}" == "n":
        notebook_dir = Path("examples")
        for hidden_file in (PROJECT_DIRECTORY / notebook_dir).glob(".*"):
            hidden_file.unlink()
        remove_file(notebook_dir / "01_intro_to_{{cookiecutter.project_slug}}.ipynb")
        remove_dir(notebook_dir)

    if "{{ cookiecutter.create_docker_file|lower }}" == "n":
        for file in [".dockerignore", "Dockerfile"]:
            remove_file(file)

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")
