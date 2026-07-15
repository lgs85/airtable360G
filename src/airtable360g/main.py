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
        config["mappings"]["grants"]
    ).to_dict(orient="records")


    locations = expand_geographic_units(
        tables["grants"],
        tables["geographic_units"],
        config["mappings"]["beneficiary_locations"]
    )

    for grant in grants_output:
        grant["beneficiaryLocation"] = locations.get(
            grant["id"],
            []
        )


    write_json(
        grants_output,
        "grants.json"
    )

if __name__ == "__main__":
    main()
