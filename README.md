# airtable360g

**airtable360g** is a Python tool for converting grant data exported from Airtable into the 360Giving Data Standard.

Rather than hard-coding field mappings, the converter uses a declarative YAML configuration to describe how Airtable fields map to the 360Giving schema. This makes it easier to adapt the converter to different Airtable bases and data models.

> **Project status:** Early development. The mapping format and API may change before the first stable release.

## Features

- Convert Airtable CSV exports to 360Giving JSON
- Declarative YAML mapping configuration
- Support for constant values and field mappings
- Support for nested JSON objects
- Expand linked Airtable records into 360Giving structures
- Designed to be extended for additional 360Giving entities

## Installation

Clone the repository and install in editable mode:

```bash
git clone git@github.com:lgs85/airtable360g.git
cd airtable360g
pip install -e .
```

## Usage

Place your exported Airtable CSV files in the `inputs/` directory.

Configure your field mappings in:

```text
mappings/example.yaml
```

Run the converter:

```bash
airtable360g
```

Generated JSON is written to the `outputs/` directory.

## Mapping

The converter is driven entirely by YAML configuration.

Simple field mapping:

```yaml
title:
  from: title
```

Constant values:

```yaml
currency:
  value: GBP
```

Nested objects:

```yaml
amountAwarded:
  type: object
  fields:
    amount:
      from: amount_committed
    currency:
      value: GBP
```

The aim is to keep Airtable-specific logic in the mapping configuration rather than in Python code wherever practical.

## Roadmap

Planned work includes:

- Complete support for the 360Giving JSON schema
- Validation against the official schema
- Direct Airtable API support
- Additional mapping types
- Automated tests

## Licence

MIT License.
