Submission summary

I implemented the Data Detective project with the following improvements to meet rubric expectations:

- Added a small CLI (`python -m src.project --file <path> --top N`) with type hints and docstrings.
- Added unit tests, including a CLI test and focused tests for `describe_text()` edge cases.
- Added GitHub Actions CI to run `pytest` on push/PR and a `requirements.txt` for reproducibility.
- Updated `README.md` with usage examples and a design note.

How to run locally

```bash
# run tests
pytest -q

# run the report on the bundled sample dataset
python -m src.project
```

Files changed: `src/project.py`, `README.md`, `tests/test_cli.py`, `tests/test_describe.py`, `.github/workflows/python-app.yml`, `requirements.txt`.

All tests pass locally and in CI. Please let me know if you'd like any stylistic or content changes before submission.
