Fixed-Width File Parser
This project provides a Python-based solution to:

Generate a fixed-width file based on specifications defined in spec.json.
Parse the fixed-width file into structured records.
Convert parsed records into a CSV file.
The workflow includes:

Unit and integration testing for reliability.
A Docker container for portability and reproducibility.
Features
Generate a fixed-width file using a JSON specification (spec.json).
Parse the file into structured records.
Export records to a CSV file.
Run the project in a Docker container.
Automated testing to validate functionality.
File Structure
plaintext
Copy code
.
├── Dockerfile                  # Docker configuration file
├── Main.py                     # Main script to execute the workflow
├── GenerateFixedWidthFile.py   # Script to generate a fixed-width file
├── ParseSpec.py                # Parse JSON spec file
├── ParseFixedWidthFile.py      # Parse fixed-width file
├── WriteToCSV.py               # Write parsed records to CSV
├── Test.py                     # Unit and integration tests
├── spec.json                   # Specification for fixed-width file
Getting Started
Prerequisites
Python 3.9+ (if running locally)
Docker (if running in a container)
Run Locally
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Run the Workflow:

bash
Copy code
python Main.py spec.json input.txt output.csv
Expected Output:
input.txt: Generated fixed-width file.
output.csv: Parsed records in CSV format.
Run Tests:

bash
Copy code
python -m unittest discover -s . -p "*Test.py"
Expected Output:
plaintext
Copy code
.....
----------------------------------------------------------------------
Ran 5 tests in 0.200s

OK
Run with Docker
Build the Docker Image:

bash
Copy code
docker build -t fixed-width-parser .
Run the Workflow in Docker:

bash
Copy code
docker run --rm -v "${PWD}:/app" fixed-width-parser spec.json input.txt output.csv
Expected Output:
plaintext
Copy code
Fixed-width file 'input.txt' generated successfully.
CSV file 'output.csv' written successfully.
Run Tests in Docker:

bash
Copy code
docker run --rm -v "${PWD}:/app" fixed-width-parser -m unittest discover -s . -p "*Test.py"
Expected Output:
plaintext
Copy code
.....
----------------------------------------------------------------------
Ran 5 tests in 0.200s

OK
Debug or Inspect Inside Docker: Launch an interactive shell inside the container:

bash
Copy code
docker run --rm -it --entrypoint sh -v "${PWD}:/app" fixed-width-parser
Use ls /app to view files.
Run commands manually, e.g.,:
bash
Copy code
python Main.py spec.json input.txt output.csv
python -m unittest discover -s . -p "*Test.py"
Testing
This project includes both unit tests and integration tests in Test.py:

Unit Tests:
Validate individual components like parse_spec, parse_fixed_width, and write_to_csv.
Integration Tests:
Validate the full workflow from file generation to CSV export.
Run tests locally or in Docker using:

bash
Copy code
python -m unittest discover -s . -p "*Test.py"
or

bash
Copy code
docker run --rm -v "${PWD}:/app" fixed-width-parser -m unittest discover -s . -p "*Test.py"
Example Workflow
Generate input.txt using spec.json:

bash
Copy code
python GenerateFixedWidthFile.py spec.json input.txt
Parse input.txt and export to output.csv:

bash
Copy code
python Main.py spec.json input.txt output.csv
Validate output in output.csv.
