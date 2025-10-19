def get_book_text(book_id):
    with open(book_id) as f:
         return f.read()
         
    

def count_words(text):
     return len(text.split())
     


def main():
     text = get_book_text("/home/adil/Bookbot/books/frankenstein.txt")
     print(f"Found {count_words(text)} total words")




main()

