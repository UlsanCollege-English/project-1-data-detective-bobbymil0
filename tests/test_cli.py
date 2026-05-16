from src.project import main


def test_cli_shows_top_and_dataset(capsys):
    # Run the CLI with a small top value to keep output predictable
    main(["--top", "3"])
    captured = capsys.readouterr()
    assert "=== Data Detective Report ===" in captured.out
    assert "Top 3 words:" in captured.out
