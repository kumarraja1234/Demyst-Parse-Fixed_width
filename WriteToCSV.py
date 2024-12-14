import csv

def write_to_csv(records, column_names, output_file, include_header, encoding):
    """
    Write parsed records to a CSV file.
    :param records: List of parsed records.
    :param column_names: List of column names.
    :param output_file: Path to the output CSV file.
    :param include_header: Whether to include the header row.
    :param encoding: Encoding of the output CSV file.
    """
    try:
        with open(output_file, 'w', newline='', encoding=encoding) as f:
            writer = csv.writer(f)
            if include_header:
                writer.writerow(column_names)  # Write header
            writer.writerows(records)  # Write data rows
        print(f"CSV file '{output_file}' written successfully.")
    except Exception as e:
        raise RuntimeError(f"Error writing to CSV file: {str(e)}")
