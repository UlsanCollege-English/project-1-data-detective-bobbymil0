from src.project import describe_text


def test_describe_empty():
    res = describe_text({})
    assert res["total_words"] == 0
    assert res["unique_words"] == 0
    assert res["most_frequent"] is None
    assert res["lexical_diversity"] == 0.0


def test_describe_single_word():
    counts = {"hello": 3}
    res = describe_text(counts)
    assert res["total_words"] == 3
    assert res["unique_words"] == 1
    assert res["most_frequent"] == ("hello", 3)
    assert res["lexical_diversity"] == round(1 / 3, 2)


def test_describe_tie_and_lexical_diversity():
    counts = {"apple": 2, "banana": 2, "carrot": 1}
    res = describe_text(counts)
    assert res["most_frequent"] in [("apple", 2), ("banana", 2)]
    assert res["lexical_diversity"] == round(3 / 5, 2)
