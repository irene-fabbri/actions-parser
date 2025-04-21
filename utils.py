import re
import json
import jsonschema
from jsonschema import validate
from .actions.exceptions import ActionError

def interpolate(input, event):
    # need to interpolate {{ key.value }}
    pattern = re.compile(r"\{\{\s*(\w+\.\w+)\s*\}\}")

    def replace(match):
        try:
            key, value = match.group(1).split('.',1)
            item = event[key][value]
            return str(item)
        except Exception:
            return ''

    return pattern.sub(replace, input)

def validateStorySchema(story_dict, schema_path="schemas/story_schema.json"):
    """
    Validates the given story dictionary against the JSON schema.

    Raises:
        ActionError: if the JSON does not conform to the schema.
    """
    try:
        with open(schema_path, "r") as schema_file:
            schema = json.load(schema_file)
        validate(instance=story_dict, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise ActionError(f"Story schema validation failed: {e.message}")
    except FileNotFoundError:
        raise ActionError(f"Schema file not found at path: {schema_path}")
    except json.JSONDecodeError as e:
        raise ActionError(f"Failed to parse schema file: {e}")