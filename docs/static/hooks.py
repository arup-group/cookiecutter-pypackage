"""Hooks for creating docs pages on-the-fly."""

import tempfile
from pathlib import Path

import jsonschema2md
import mkdocs
import yaml
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
    files.append(_schema2md(config))

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


def _schema2md(config: dict) -> File:
    """Generate overview over configuration schema and add to mkdoc's files.

    Args:
        config (dict): MKDocs project configuration.

    Returns:
        File: File object.
    """
    path_to_schema: Path = Path.cwd() / "schema.yaml"
    path_to_md: Path = Path(TEMPDIR.name) / "schema.md"

    parser = jsonschema2md.Parser()
    parser.tab_size = 4
    schema = yaml.safe_load(path_to_schema.read_text())
    schema["properties"].pop("__prompts__")
    lines = parser.parse_schema(schema)
    lines = _customise_markdown(lines)

    path_to_md.write_text("\n".join(lines))

    return File(
        path="schema.md",
        src_dir=TEMPDIR.name,
        dest_dir=config["site_dir"],
        use_directory_urls=config["use_directory_urls"],
    )


def _customise_markdown(lines: list) -> list:
    """Clean up rendered Schema so that it doesn't read as a schema in the docs.

    Args:
        lines (list): rendered schema as a list of line strings

    Returns:
        list: Cleaned, rendered schema as a list of line strings
    """
    # 1. Change headline
    assert lines[0] == "# JSON Schema\n\n"
    lines[0] = "# Configuration values\n\n"

    # 2. Remove main description and subheadline
    assert lines[2] == "## Properties\n\n"
    del lines[2]

    return lines
