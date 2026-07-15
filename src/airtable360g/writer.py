import json
from pathlib import Path


def write_json(data, filename):
    output_path = Path("outputs")
    output_path.mkdir(exist_ok=True)

    with open(output_path / filename, "w") as f:
        json.dump(data, f, indent=2)
