import pandas as pd

def transform_table(source, mapping):
    output = pd.DataFrame()

    for output_field, rule in mapping.items():
        if "from" in rule:
            output[output_field] = source[rule["from"]]

        elif "value" in rule:
            output[output_field] = rule["value"]

    return output

def expand_geographic_units(source_grants, geographic_units, mapping):
    locations_by_grant = {}

    scope_field = mapping["scope_field"]

    for _, grant in source_grants.iterrows():
        locations = []

        scope = grant[scope_field]

        for rule in mapping["rules"]:
            if scope == rule["when"]:

                if "create" in rule:
                    locations.append(rule["create"])

                elif "expand_from" in rule:
                    linked_field = rule["expand_from"]

                    codes = str(grant[linked_field]).split(",")

                    for code in codes:
                        code = code.strip()

                        matches = geographic_units[
                            geographic_units["code"] == code
                        ]

                        for _, geo in matches.iterrows():
                            locations.append({
                                "geographicCode": geo["code"],
                                "geographicCodeType": geo["type"],
                                "name": geo["name"],
                            })

        locations_by_grant[grant["id_360g"]] = locations

    return locations_by_grant
