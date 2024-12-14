import json

def parse_spec(spec_file):
    """
    Parse the specification JSON file to extract column names, offsets, and encodings.
    :param spec_file: Path to the spec.json file.
    :return: Tuple containing column names, offsets, fixed-width encoding, delimited encoding, and header flag.
    """
    with open(spec_file, 'r') as f:
        spec = json.load(f)
    
    # Extract required fields from the JSON spec
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))  # Convert offsets to integers
    fixed_width_encoding = spec["FixedWidthEncoding"]
    delimited_encoding = spec["DelimitedEncoding"]
    include_header = spec["IncludeHeader"] == "True"
    
    return column_names, offsets, fixed_width_encoding, delimited_encoding, include_header

