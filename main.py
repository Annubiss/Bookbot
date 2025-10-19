from stats import count_words
from stats import count_characters
def get_book_text(book_id):
    with open(book_id) as f:
         return f.read()
         
    
     


def main():
     text = get_book_text("/home/adil/Bookbot/books/frankenstein.txt")
     print(f"Found {count_words(text)} total words")
     print(count_characters(text))




main()

