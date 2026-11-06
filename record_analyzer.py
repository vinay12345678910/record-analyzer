"""
Record Analyzer - Validates and summarizes course records from JSON files.

This module provides functionality to:
- Load course records from JSON files
- Validate record structure and data types
- Filter records based on minimum score threshold
- Calculate statistics (total, average, counts)
- Export summary results to JSON

Author: Vinay
License: MIT
"""

import json


def is_valid_record(record):
    """
    Validate a single course record.

    Args:
        record: A dictionary containing course information

    Returns:
        bool: True if record is valid, False otherwise

    Validation Rules:
        - Must be a dictionary
        - Must contain 'course' and 'score' keys
        - Course must be a non-empty string
        - Score must be a number (not boolean) between 0 and 100 inclusive
    """
    if not isinstance(record, dict):
        return False

    if "course" not in record or "score" not in record:
        return False

    if not isinstance(record["course"], str):
        return False

    if record["course"].strip() == "":
        return False

    if isinstance(record["score"], bool):
        return False

    if not isinstance(record["score"], (int, float)):
        return False

    if record["score"] < 0 or record["score"] > 100:
        return False

    return True

#print(is_valid_record({"course" :"python", "score": 80}))
#print(is_valid_record({"course": "python"}))
#print(is_valid_record({"course": "test", "score": -1}))
#print(is_valid_record({"course": "test", "score": 0}))
#print(is_valid_record({"course": "test", "score": 100}))
#print(is_valid_record({"course": "test", "score": 101}))

def summarize_records(records, minimum):
    """
    Summarize valid records that meet the minimum score threshold.

    Args:
        records (list): List of course record dictionaries
        minimum (int/float): Minimum score threshold for acceptance

    Returns:
        dict: Summary with keys:
            - accepted (int): Count of valid records >= minimum
            - ignored (int): Count of invalid or below-threshold records
            - total (int/float): Sum of all accepted scores
            - average (float): Average of accepted scores (0 if none accepted)
    """
    accepted = 0
    ignored = 0
    total = 0

    for r in records:
        if not is_valid_record(r):
            ignored += 1
            continue

        if r["score"] < minimum:
            ignored += 1
            continue

        accepted += 1
        total += r["score"]

    average = total / accepted if accepted > 0 else 0

    return {
        "accepted": accepted,
        "ignored": ignored,
        "total": total,
        "average": average
    }

#print(summarize_records(records, 60))

def load_records(filename):
    """
    Load and validate course records from a JSON file.

    Args:
        filename (str): Path to the JSON file containing records

    Returns:
        list or None: List of records if successful, None if error occurred

    Error Handling:
        - Prints "File not Found" if file doesn't exist
        - Prints "Invalid JSON" if file contains malformed JSON
        - Prints "Expected a list of records" if root element is not a list
    """
    try:
        with open(filename, "r") as file:
            records = json.load(file)

    except FileNotFoundError:
        print("File not Found")
        return None

    except json.JSONDecodeError:
        print("Invalid JSON")
        return None

    if not isinstance(records, list):
        print("Expected a list of records")
        return None

    return records

def main():
    """
    Main entry point for the record analyzer.

    Process:
        1. Load records from 'records.json'
        2. Analyze records with minimum score of 60
        3. Print summary to console
        4. Export summary to 'summary.json'
    """
    print("record analyzer started")

    loaded_records = load_records("records.json")

    if loaded_records is not None:
        summary = summarize_records(loaded_records, 60)
        print("summary =", summary)

        with open("summary.json", "w") as file:
            json.dump(summary, file, indent=4)
    else:
        print("summary skipped")

if __name__ == "__main__":
	main()
