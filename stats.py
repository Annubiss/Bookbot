def count_words(text):
         return len(text.split())

def count_characters(text):
    s = text.lower()
    from collections import Counter
    counts = Counter(s)
    return dict(counts)