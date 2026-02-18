from collections import Counter
import re

def repeated_words(titles):
    words = []
    for t in titles:
        words += re.findall(r"\b[a-zA-Z]+\b", t.lower())

    count = Counter(words)

    # Remove common stop words (makes analysis meaningful)
    stop_words = {
        "the", "a", "an", "and", "of", "to", "in", "for",
        "on", "at", "with", "is", "that", "this"
    }

    filtered = {
        w: c for w, c in count.items()
        if c >= 2 and w not in stop_words
    }

    return filtered
