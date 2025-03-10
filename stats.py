def get_book_text(books):
    with open(books) as file:
        return file.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    return text

def word_counter():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = text.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")
