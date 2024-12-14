from ParseSpec import parse_spec
from ParseFixedWidthFile import parse_fixed_width
from WriteToCSV import write_to_csv
import json
import random
import string


def generate_fixed_width_file(spec_file, output_file, num_records=10):
    """
    Generate a fixed-width file based on the provided spec.
    """
    try:
        with open(spec_file, 'r') as f:
            spec = json.load(f)

        offsets = list(map(int, spec["Offsets"]))
        encoding = spec["FixedWidthEncoding"]

        # Helper function to generate random field content
        def random_field(length):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        with open(output_file, 'w', encoding=encoding) as f:
            for _ in range(num_records):
                # Create a line based on offsets
                line = ''.join(random_field(length).ljust(length) for length in offsets)
                f.write(line + '\n')

        print(f"Fixed-width file '{output_file}' generated successfully.")
    except Exception as e:
        raise RuntimeError(f"Error generating fixed-width file: {str(e)}")


def main(spec_file, fixed_width_file, output_csv, num_records=10):
    """
    Main function to handle fixed-width file generation, parsing, and CSV conversion.
    """
    # Step 1: Generate the fixed-width file
    generate_fixed_width_file(spec_file, fixed_width_file, num_records)

    # Step 2: Parse the spec
    column_names, offsets, fixed_width_encoding, delimited_encoding, include_header = parse_spec(spec_file)

    # Step 3: Parse the fixed-width file
    records = parse_fixed_width(fixed_width_file, offsets, fixed_width_encoding)

    # Step 4: Write to CSV
    write_to_csv(records, column_names, output_csv, include_header, delimited_encoding)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python Main.py <spec_file> <fixed_width_file> <output_csv>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
