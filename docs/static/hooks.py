from pathlib import Path

import jsonschema2md
import mkdocs.plugins
import yaml
from mkdocs.structure.files import File


# Bump priority to ensure files are moved before jupyter notebook conversion takes place
@mkdocs.plugins.event_priority(50)
def on_files(files: list, config: dict, **kwargs):
    """
    1. Link top-level files to mkdocs files.
    2. Clean up YAML schema
    """
    files.append(_new_file("./CHANGELOG.md", config))
    files.append(_new_file("./CONTRIBUTING.md", config))
    files.append(_new_file("./README.md", config))
    files.append(_schema2md(config))

    return files


def _new_file(path: str | Path, config: dict) -> File:
    return File(
        path=path,
        src_dir=".",
        dest_dir=config["site_dir"],
        use_directory_urls=config["use_directory_urls"],
    )


def _schema2md(config: dict):
    """Generate overview over configuration schema and add to mkdoc's files."""
    path_to_schema: Path = Path.cwd() / "schema.yaml"
    path_to_md: Path = Path.cwd() / config["site_dir"] / "schema.md"

    parser = jsonschema2md.Parser()
    parser.tab_size = 4
    schema = yaml.safe_load(path_to_schema.read_text())

    lines = parser.parse_schema(schema)
    lines = _customise_markdown(lines)
    path_to_md.write_text("\n".join(lines))

    return File(
        path="schema.md",
        src_dir=config["site_dir"],
        dest_dir=config["site_dir"],
        use_directory_urls=config["use_directory_urls"],
    )


def _customise_markdown(lines: list) -> list:
    # 1. Change headline
    assert lines[0] == "# JSON Schema\n\n"
    lines[0] = "# Configuration values\n\n"

    # 2. Remove main description and subheadline
    assert lines[2] == "## Properties\n\n"
    del lines[2]

    return lines
