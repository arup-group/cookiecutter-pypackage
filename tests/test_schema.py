import json
from pathlib import Path

import jinja2
import jsonschema
import pytest
import yaml


@pytest.fixture
def schema():
    schema_path = Path(__file__).parent / ".." / "schema.yaml"
    return yaml.safe_load(schema_path.read_text())


@pytest.fixture
def config():
    config_path = Path(__file__).parent / ".." / "json"
    config_with_jinja_elements = json.loads(config_path.read_text())
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(config_path.parent),
        lstrip_blocks=True,
        trim_blocks=True,
        keep_trailing_newline=True,
    )
    rendered = env.get_template(config_path.name).render(
        cookiecutter={k: v for k, v in config_with_jinja_elements.items() if "{{" not in v}
    )
    return json.loads(rendered)


def test_config(config, schema):
    jsonschema.validate(config, schema)


def test_schema(schema):
    # We set the metaschema 'additionalProperties' to False to create a 'strict' schema checker,
    # which will fail on typos
    jsonschema.Draft7Validator.META_SCHEMA["additionalProperties"] = False
    jsonschema.Draft7Validator.check_schema(schema)
