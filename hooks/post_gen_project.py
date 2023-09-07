#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd().absolute()


def remove_file(filepath: Path | str):
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
        assert (PROJECT_DIRECTORY / "examples").exists()
        for hidden_file in (PROJECT_DIRECTORY / "examples").glob(".*"):
            hidden_file.unlink()
        remove_dir("examples")

    if "{{ cookiecutter.create_docker_file|lower }}" == "n":
        for file in [".dockerignore", "Dockerfile"]:
            remove_file(file)

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")
