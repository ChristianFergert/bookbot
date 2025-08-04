from stats import get_word_count, get_character_counts, sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    chars_dict = get_character_counts(text)
    sorted_chars_dict = sort_dict(chars_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for dict in sorted_chars_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    

def get_book_text(filepath):
    with open(filepath) as file:
        filecontent = file.read()
    return filecontent


main()
