import json

print("record analyzer started")

def is_valid_record(record):
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

loaded_records = load_records("records.json")

if loaded_records is not None:
    summary = summarize_records(loaded_records, 60)
    print("summary =", summary)

    with open("summary.json", "w") as file:
        json.dump(summary, file, indent=4)
else:
    print("summary skipped")
