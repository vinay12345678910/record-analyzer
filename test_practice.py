import tempfile

from record_analyzer import summarize_records, load_records

records = [
    {"course": "python", "score": 80},
    {"course": "SQL", "score": 50},
]

expected = {"accepted": 1, "ignored": 1, "total": 80, "average": 80.0}
actual = summarize_records(records, 60)

assert actual == expected

with tempfile.TemporaryDirectory() as folder:
    missing_path = f"{folder}/missing.json"
    result = load_records(missing_path)
    assert result is None

with tempfile.TemporaryDirectory() as folder:
    invalid_path = f"{folder}/invalid.json"
    with open(invalid_path, "w", encoding = "utf-8") as file:
        file.write("[")
    result = load_records(invalid_path)
    assert result is None
