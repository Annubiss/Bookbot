import unicodedata
import sys
from stats import count_words
from stats import count_characters
from stats import sort_items 
def get_book_text(book_id):
    with open(book_id) as f:
         return f.read()
         
    
     


def main():
     if len(sys.argv) < 2:
          print("Usage: python3 main.py <path_to_book>")
          raise SystemExit(1)
     
     book_path = sys.argv[1]
     text = get_book_text(book_path)
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

