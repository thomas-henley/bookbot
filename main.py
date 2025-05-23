import sys
from stats import *

def get_book_text(filepath):
    book_text = None
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def print_report(list):
    for entry in list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = count_words(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    report = sort_characters(count_characters(book))
    print_report(report)


main()