import sys

from stats import get_num_words, get_character_count, get_sorted_dict

def get_books_text(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1] 
    book_content = get_books_text(book_path)
    num_words = get_num_words(book_content)
    char_count = get_character_count(book_content) 
    sorted_count = get_sorted_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    for letter_count in sorted_count:
        letter = letter_count.get("letter")
        count = letter_count.get("count")
        if letter.isalpha():
            print(f"{letter}: {count}")

main()
