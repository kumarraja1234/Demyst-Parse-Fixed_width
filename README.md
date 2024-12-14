# Fixed-Width File Parser

This project provides a Python-based solution to:

1. **Generate a fixed-width file** based on specifications defined in `spec.json`.
2. **Parse the fixed-width file** into structured records.
3. **Convert parsed records into a CSV file**.

The workflow includes:
- Unit and integration testing for reliability.
- A Docker container for portability and reproducibility.


## File Structure
```
├── Dockerfile # Docker configuration file
├── Main.py # Main script to execute the workflow
├── ParseSpec.py # Parse JSON spec file
├── ParseFixedWidthFile.py # Parse fixed-width file
├── WriteToCSV.py # Write parsed records to CSV
├── Test.py # Unit and integration tests
├── spec.json # Specification for fixed-width file
```

---

## Getting Started

### Prerequisites

- **Python 3.9+** (if running locally)
- **Docker** (if running in a container)

---

### Run Locally

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Run the Workflow**:
   ```bash
   python Main.py spec.json input.txt output.csv
   ```
   Expected Output:
    ```
    - input.txt: Generated fixed-width file.
    - output.csv: Parsed records in CSV format.
   ```

3. **Run Tests**:
   ```bash
    python -m unittest discover -s . -p "*Test.py"
   ```
   Expected Output:
    
    ```
    ----------------------------------------------------------------------
    Ran 5 tests in 0.200s
    OK
    ```

### Run with Docker

1. Build the Docker Image:

```bash
docker build -t fixed-width-parser .
```

2. Run the Workflow in Docker:
   ```bash
   docker run --rm -v "${PWD}:/app" fixed-width-parser spec.json input.txt output.csv
   ```
   Expected Output:
    ```
      Fixed-width file 'input.txt' generated successfully.
      CSV file 'output.csv' written successfully.
   ```

3. Run Tests in Docker:

    ```bash
    docker run --rm -v "${PWD}:/app" fixed-width-parser -m unittest discover -s . -p "*Test.py"
   ```
   Expected Output:
    
    ```
    ----------------------------------------------------------------------
    Ran 5 tests in 0.200s
    OK
    ```
4. Debug or Inspect Inside Docker: Launch an interactive shell inside the container:

  ```bash
  docker run --rm -it --entrypoint sh -v "${PWD}:/app" fixed-width-parser
  ```

- Use ls /app to view files.
- Run commands manually, e.g.,:

```bash
python Main.py spec.json input.txt output.csv
python -m unittest discover -s . -p "*Test.py"
```

### Testing

This project includes both unit tests and integration tests in Test.py:

- Unit Tests:
   Validate individual components like parse_spec, parse_fixed_width, and write_to_csv.
- Integration Tests:
   Validate the full workflow from file generation to CSV export.
  
Run tests locally or in Docker using:

```bash
python -m unittest discover -s . -p "*Test.py"
```
or
```bash
docker run --rm -v "${PWD}:/app" fixed-width-parser -m unittest discover -s . -p "*Test.py"
```
# Note
In `Test.py` os.remove() is used to delete files after each test, leaving no residual files. You can check the input and output files generated for Unit and Integration testing by discarding os.remove() from `Test.py`
