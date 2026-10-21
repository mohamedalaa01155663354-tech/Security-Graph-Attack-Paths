# Security Graph & Attack Paths

## Project Overview
This project analyzes cloud security configurations and identifies potential attack paths to sensitive resources using Python and NetworkX.

## Objectives
- Build a security graph representing cloud resources and relationships.
- Identify potential attack paths from the Internet to sensitive S3 buckets.
- Compare attack paths before and after configuration changes.
- Export graph data in Cytoscape-compatible JSON format.
- Test security scenarios using automated tests.

## Technologies
- Python
- NetworkX
- AWS Boto3
- AWS Lambda
- Amazon S3
- Pytest
- Cytoscape.js (for visualization integration)

## Project Structure
- `src/attack_paths.py`: Graph construction and attack path analysis.
- `src/lambda_function.py`: Lambda entry point and result handling.
- `tests/test_attack_paths.py`: Automated tests.
- `requirements.txt`: Project dependencies.

## Run Tests
Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the tests:

```bash
python -m pytest -v
```

## Current Scope
The current implementation analyzes a predefined JSON snapshot. Integration with live AWS resource discovery and complete IAM policy evaluation requires additional implementation and testing.

## Disclaimer
This project is intended for educational cloud security analysis and defensive security testing.
