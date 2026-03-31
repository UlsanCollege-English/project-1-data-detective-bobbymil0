from src.project import tokenize, count_words, get_top_n

def test_count_words_normal():
    words = ["hello", "world", "hello"]
    result = count_words(words)
    assert result["hello"] == 2
    assert result["world"] == 1

def test_empty_input():
    words = []
    result = count_words(words)
    assert result == {}

def test_case_handling():
    words = tokenize("Hello hello")
    result = count_words(words)
    assert result["hello"] == 2

def test_top_n():
    words = ["a", "b", "a", "c", "a", "b"]
    counts = count_words(words)
    top = get_top_n(counts, 1)
    assert top[0][0] == "a"