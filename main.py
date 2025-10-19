import unicodedata
from stats import count_words
from stats import count_characters
from stats import sort_items 
def get_book_text(book_id):
    with open(book_id) as f:
         return f.read()
         
    
     


def main():
     
     text = get_book_text("/home/adil/Bookbot/books/frankenstein.txt")
     number_of_char = count_characters(text)
     counts = sort_items(number_of_char)                 # list[(char, count)]
     lines  = [f"{ch:}: {cnt:}" for ch, cnt in counts if ch.isalpha()]  # pretty rows (aligned, with ,)
     table  = "\n".join(lines)
     print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count_words(text)} total words
--------- Character Count -------
{table}""")




main()

