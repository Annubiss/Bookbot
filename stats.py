def count_words(text):
         return len(text.split())

def count_characters(text):
    s = text.lower()
    from collections import Counter
    counts = Counter(s)
    return dict(counts)




def sort_items(items):
        return sorted(items.items(), key=lambda item: item[1], reverse=True)