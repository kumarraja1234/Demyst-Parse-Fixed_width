import unittest
import os
from ParseSpec import parse_spec
from ParseFixedWidthFile import parse_fixed_width
from WriteToCSV import write_to_csv
from Main import generate_fixed_width_file, main

class TestFixedWidthWorkflow(unittest.TestCase):
    # Unit tests for individual components
    def test_parse_spec(self):
        column_names, offsets, _, _, include_header = parse_spec('spec.json')
        self.assertEqual(len(column_names), 10)
        self.assertEqual(len(offsets), 10)
        self.assertTrue(include_header)

    def test_parse_fixed_width(self):
        # Use a unique test input file
        offsets = [5, 12, 3, 2, 13, 7, 10, 13, 20, 13]
        test_file = 'unit_test_input.txt'
        generate_fixed_width_file('spec.json', test_file, num_records=2)
        records = parse_fixed_width(test_file, offsets, 'windows-1252')
        self.assertGreater(len(records), 0)
        self.assertEqual(len(records[0]), len(offsets))
        os.remove(test_file)  # Cleanup after test

    def test_write_to_csv(self):
        # Use a unique output file
        records = [['abcde', '123456789012'], ['vwxyz', '987654321098']]
        output_file = 'unit_test_output.csv'
        write_to_csv(records, ['f1', 'f2'], output_file, True, 'utf-8')
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 3)  # Header + 2 data rows
        os.remove(output_file)  # Cleanup after test

    # Integration tests for the workflow
    def test_generate_fixed_width_file(self):
        input_file = 'test_generate_fixed_width_input.txt'
        generate_fixed_width_file('spec.json', input_file, num_records=5)
        self.assertTrue(os.path.exists(input_file))
        os.remove(input_file)  # Cleanup after test

    def test_main_workflow(self):
        input_file = 'test_main_workflow_input.txt'
        output_file = 'test_main_workflow_output.csv'
        main('spec.json', input_file, output_file, num_records=5)
        self.assertTrue(os.path.exists(input_file))
        self.assertTrue(os.path.exists(output_file))
        os.remove(input_file)  # Cleanup after test
        os.remove(output_file)  # Cleanup after test

if __name__ == '__main__':
    unittest.main()
