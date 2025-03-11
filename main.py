
from stats import word_counter, char_counter, sort_list


def get_book_text(path):
    with open(path) as file:
        return file.read()

path = "books/frankenstein.txt"
text = get_book_text(path)
num_words = word_counter(text)
char_dict = char_counter(text)


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    to_print = sort_list(char_dict)
    for i in to_print:
        character = list(i.keys())[0]
        if character.isalpha():
            count = i[character]
            print(f"{character}: {count}")

    print("============= END ===============")

main()