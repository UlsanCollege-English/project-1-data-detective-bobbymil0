import re

def load_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def get_top_n(word_counts, n):
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

# RUN (for testing manually)
if __name__ == "__main__":
    text = load_text("data/sample.txt")
    words = tokenize(text)
    counts = count_words(words)
    top = get_top_n(counts, 5)

    print("Top words:")
    for word, count in top:
        print(word, count)

    # BONUS
    print("\nMost frequent word:", top[0])

    print("\nTotal words:", len(words))
    print("Unique words:", len(counts))