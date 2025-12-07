import sys
from stats import get_num_words, create_list_num_chars

def get_book_text(filename):
    with open(filename, 'r') as f:
        return f.read()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book = sys.argv[1]
    # print(get_book_text(book))
    num_words = get_num_words(book)
    num_chars = create_list_num_chars(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for items in num_chars:
        print(f"{items['char']}: {items['num']}")