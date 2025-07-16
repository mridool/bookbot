import sys
from stats import get_num_words, get_char_counts, get_sorted_char_counts

def get_book_text(file_path):
    file_contents = ""

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def print_result(book_path, num_words, char_dict_list):
    print("="*12 + " BOOKBOT " + "="*12)
    
    print(f'Analyzing book found at {book_path}')

    print("-"*11 + " Word Count" + "-"*10)

    print(f'Found {num_words} total words')

    print("-"*9 + " Character Count " + "-"*7)

    for c_dict in char_dict_list:
        print(f'{c_dict["char"]}: {c_dict["num"]}')

    print("=" * 13 + " END " + "=" * 15)



def main():
    print(sys.argv)

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)

    num_words = get_num_words(book_contents)
    char_count_dict = get_char_counts(book_contents)
    char_count_sorted_dict = get_sorted_char_counts(book_contents)

    print_result(book_path, num_words, char_count_sorted_dict)


main()