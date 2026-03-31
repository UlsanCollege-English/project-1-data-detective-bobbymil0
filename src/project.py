from pathlib import Path
import re


def load_text(file_path):
    """Return the full text contents of a file."""
    return Path(file_path).read_text(encoding="utf-8")


def tokenize(text):
    """Normalize text and split it into lowercase word tokens."""
    return re.findall(r"[a-z0-9']+", text.lower())


def count_words(words):
    """Count how many times each word appears."""
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def top_n_words(word_counts, n):
    """Return the top n words sorted by frequency, then alphabetically."""
    if n <= 0:
        return []
    sorted_words = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:n]


def get_top_n(word_counts, n):
    """Backward-compatible wrapper used by the tests."""
    return top_n_words(word_counts, n)


def describe_text(word_counts):
    """Compute one extra insight about the dataset."""
    total_words = sum(word_counts.values())
    unique_words = len(word_counts)
    most_frequent = top_n_words(word_counts, 1)[0] if word_counts else None
    lexical_diversity = round(unique_words / total_words, 2) if total_words else 0.0

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "most_frequent": most_frequent,
        "lexical_diversity": lexical_diversity,
    }


def main():
    """Run the word-frequency analysis on the sample dataset."""
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "sample.txt"

    text = load_text(data_path)
    words = tokenize(text)
    counts = count_words(words)
    top_words = top_n_words(counts, 5)
    summary = describe_text(counts)

    print("=== Data Detective Report ===")
    print(f"Dataset: {data_path.name}")

    if not words:
        print("\nThe file is empty, so there are no words to analyze.")
        return

    print("\nTop 5 words:")
    for index, (word, count) in enumerate(top_words, start=1):
        print(f"{index}. {word}: {count}")

    print("\nExtra insight:")
    print(
        f"- Most frequent word: {summary['most_frequent'][0]} "
        f"({summary['most_frequent'][1]} times)"
    )
    print(f"- Total words: {summary['total_words']}")
    print(f"- Unique words: {summary['unique_words']}")
    print(f"- Lexical diversity: {summary['lexical_diversity']}")


if __name__ == "__main__":
    main()