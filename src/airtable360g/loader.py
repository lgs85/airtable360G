from pathlib import Path
import pandas as pd


def load_inputs(config):
    tables = {}

    for name, details in config["inputs"].items():
        file_path = Path("samples") / details["file"]
        tables[name] = pd.read_csv(file_path)

    return tables
