# Record Analyzer

A Python script that reads course records from `records.json` and summarizes scores of 60 or higher. Each valid record has a non-empty course name and a numeric score from 0 to 100. Invalid records and scores below 60 count as ignored.

## Run

From the repository folder, run:

```bash
python3 record_analyzer.py
```

The script prints the accepted and ignored counts, the total of accepted scores, and their average. It also saves those results to `summary.json`. No external packages are required.

## Test

```bash
python3 -B test_practice.py
```

The tests check the summary, missing files, and malformed JSON.

## License

[MIT](LICENSE)
