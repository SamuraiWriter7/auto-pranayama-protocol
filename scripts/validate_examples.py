from pathlib import Path

import json
import yaml
from jsonschema import Draft7Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


VALIDATION_TARGETS = [
    {
        "name": "Auto-Pranayama Record",
        "schema": ROOT / "schemas" / "auto-pranayama-record.schema.json",
        "example": ROOT / "examples" / "auto-pranayama-record.example.yaml",
    }
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_target(target: dict) -> bool:
    name = target["name"]
    schema_path = target["schema"]
    example_path = target["example"]

    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft7Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

    if errors:
        print(f"[error] {name} validation failed")
        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"  - path: {path}")
            print(f"    message: {error.message}")
        return False

    print(f"[ok] {example_path.name} is valid")
    return True


def main() -> int:
    all_valid = True

    for target in VALIDATION_TARGETS:
        if not validate_target(target):
            all_valid = False

    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())

