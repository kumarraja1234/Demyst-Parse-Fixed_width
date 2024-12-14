def parse_fixed_width(file_path, offsets, encoding):
    """
    Parse a fixed-width file into structured records based on field offsets.
    :param file_path: Path to the fixed-width file.
    :param offsets: List of field offsets (lengths for each column).
    :param encoding: Encoding of the input fixed-width file.
    :return: List of parsed records (each record is a list of fields).
    """
    try:
        records = []
        
        with open(file_path, 'r', encoding=encoding) as f:
            for line in f:
                start = 0
                record = []
                for offset in offsets:
                    field = line[start:start+offset].strip()  # Extract field and strip whitespace
                    record.append(field)
                    start += offset
                records.append(record)
        
        return records
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Fixed-width file '{file_path}' not found.")
    except Exception as e:
        raise RuntimeError(f"Error parsing fixed-width file: {str(e)}")
