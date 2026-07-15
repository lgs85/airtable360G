from pathlib import Path

from .config import load_config
from .loader import load_inputs
from .transformer import transform_table, expand_geographic_units
from .writer import write_json


def main():
    config = load_config(Path("mappings/example.yaml"))

    tables = load_inputs(config)

    grants_output = transform_table(
        tables["grants"],
        config["mappings"]["grant"]
    ).to_dict(orient="records")

    package = {
	    "grants": grants_output
    }

    write_json(
	    package,
	    "grants.json"
    )

if __name__ == "__main__":
    main()
