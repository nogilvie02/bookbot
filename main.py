import sys
from stats import get_num_words, get_chars_dict, sort_num_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    print(f"Analyzing book found at {path_to_book}...")

    print("----------- Word Count ----------")
    total_words = get_num_words(book_text)
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    chars = get_chars_dict(book_text)
    sorted_chars = sort_num_chars(chars)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()