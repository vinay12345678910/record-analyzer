# Record Analyzer

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python tool that validates, filters, and analyzes course records from JSON files. It automatically calculates statistics for passing scores and generates structured summaries.

## Features

- ✅ **JSON Validation** - Robust error handling for missing files, malformed JSON, and invalid data structures
- 🔍 **Record Validation** - Ensures all records contain required fields with proper data types
- 📊 **Score Filtering** - Configurable minimum score threshold (default: 60)
- 📈 **Statistical Analysis** - Calculates accepted/ignored counts, totals, and averages
- 💾 **Export Results** - Generates `summary.json` with analysis results

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vinay12345678910/record-analyzer.git
cd record-analyzer
```

2. Ensure you have Python 3.6 or higher:
```bash
python --version
```

No external dependencies required - uses only Python standard library.

## Usage

### Basic Usage

Place your course records in `records.json` and run:

```bash
python record_analyzer.py
```

### Input Format

Create a `records.json` file with an array of course records:

```json
[
    {"course": "python", "score": 80},
    {"course": "java", "score": 60},
    {"course": "javascript", "score": 95},
    {"course": "ML", "score": 45}
]
```

### Output

The script prints progress to console and creates `summary.json`:

```json
{
    "accepted": 3,
    "ignored": 1,
    "total": 235,
    "average": 78.33
}
```

**Console output:**
```
record analyzer started
summary = {'accepted': 3, 'ignored': 1, 'total': 235, 'average': 78.33}
```

## Validation Rules

Records are validated against the following criteria:

- ✅ Must be a dictionary/object
- ✅ Must contain both `"course"` and `"score"` fields
- ✅ Course name must be a non-empty string
- ✅ Score must be a number (int or float)
- ✅ Score must be between 0 and 100 (inclusive)
- ✅ Records below the minimum threshold (60) are ignored

### Examples of Valid Records
```json
{"course": "python", "score": 80}     ✅
{"course": "data science", "score": 100}  ✅
{"course": "ML", "score": 0}          ✅
```

### Examples of Invalid Records
```json
{"course": "test"}                    ❌ Missing score
{"score": 85}                         ❌ Missing course
{"course": "", "score": 90}           ❌ Empty course name
{"course": "test", "score": 101}      ❌ Score out of range
{"course": "test", "score": -10}      ❌ Negative score
```

## Error Handling

The analyzer handles various error scenarios gracefully:

| Error | Output | Behavior |
|-------|--------|----------|
| Missing file | `"File not Found"` | Skips summary generation |
| Invalid JSON syntax | `"Invalid JSON"` | Skips summary generation |
| Non-list root element | `"Expected a list of records"` | Skips summary generation |
| Empty list | Generates summary with zeros | Creates `summary.json` |
| Invalid records | Counted in `"ignored"` field | Continues processing |

## Project Structure

```
record-analyzer/
├── record_analyzer.py    # Main analyzer script
├── test_practice.py      # Unit tests
├── records.json          # Input data file
├── summary.json          # Generated output (created after running)
├── README.md             # This file
├── LICENSE               # MIT License
└── .gitignore            # Git ignore rules
```

## Running Tests

Execute the test suite:

```bash
python test_practice.py
```

Or using unittest:

```bash
python -m unittest test_practice.py
```

## Use Cases

- 📚 **Educational Institutions** - Analyze student performance across courses
- 🎓 **Training Programs** - Track completion rates and average scores
- 📊 **Data Validation** - Clean and validate course records before further processing
- 🔄 **Batch Processing** - Automated analysis of course results

## Configuration

To change the minimum passing score, modify line 89 in `record_analyzer.py`:

```python
summary = summarize_records(loaded_records, 60)  # Change 60 to your threshold
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Vinay**
- GitHub: [@vinay12345678910](https://github.com/vinay12345678910)

## Acknowledgments

- Built with Python standard library only
- Designed for simplicity and reliability

---

**Last Updated:** November 2026
