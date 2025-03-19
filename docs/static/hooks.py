"""Hooks for creating docs pages on-the-fly."""

import tempfile
from pathlib import Path

import mkdocs
from mkdocs.structure.files import File

TEMPDIR = tempfile.TemporaryDirectory()


def on_files(files: list, config: dict, **kwargs) -> list:
    """Update MKDocs pages.

    1. Link top-level files to mkdocs files.
    2. Clean up YAML schema

    Args:
        files (list): List of MKDocs project files.
        config (dict): MKDocs project configuration.
        **kwargs: necessary to capture inputs provided by MKDocs when it calls this function.

    Returns:
        list: Updated list of MKDocs project files.
    """
    files.append(_new_file("./CHANGELOG.md", config))
    files.append(_new_file("./CONTRIBUTING.md", config))
    files.append(_new_file("./README.md", config))

    return files


@mkdocs.plugins.event_priority(-100)
def on_post_build(**kwargs):
    """After mkdocs has finished building the docs, remove the temporary directory of markdown files.

    Args:
        **kwargs (Config): mkdocs config dictionary (unused).
    """
    TEMPDIR.cleanup()


def _new_file(path: str | Path, config: dict) -> File:
    """Create an MKDocs File object.

    Args:
        path (str | Path): Path to file.
        config (dict): MKDocs project configuration.

    Returns:
        File: File object.
    """
    return File(
        path=path,
        src_dir=".",
        dest_dir=config["site_dir"],
        use_directory_urls=config["use_directory_urls"],
    )
