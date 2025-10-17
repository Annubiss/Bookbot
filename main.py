
def get_book_text(book_id):
    with open(book_id) as f:
         file_contents = f.read()
         return file_contents
    

def main():
     print(get_book_text("/home/adil/Bookbot/books/frankenstein.txt"))




main()

