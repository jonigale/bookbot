from stats import get_words, count_characters, sorted_list
import sys

def get_book_text(path):
    file_contents = ''
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def usage():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    usage()
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_words(text)
    chars = count_characters(text)
    sortlist = sorted_list(chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for i in sortlist:
        if not i['char'].isalpha():
            continue
        else:
            print(f"{i['char']}: {i['count']}")
    print("============= END ===============")

main()
        
