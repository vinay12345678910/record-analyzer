# Record Analyzer

A Python script that reads course records from a JSON file, validates them,
and summarizes scores of 60 or above.

## Requirements
- Python 3
- No extra packages required

## How to run
Open a terminal in the record-analyzer folder and run:

```bash
python record_analyzer.py
```

The folder must contain record_analyzer.py and records.json.

## Sample result
For the supplied sample records:
- Accepted: 2
- Ignored: 1
- Total: 140
- Average: 70.0

## Input checks
- Empty list: prints a summary with all zeros.
- Missing file: prints "File not Found" and skips the summary.
- Broken JSON: prints "Invalid JSON" and skips the summary.
- JSON that is not a list: prints "Expected a list of records" and skips the summary.
- Scores must be between 0 and 100 inclusive; records outside this range are ignored.