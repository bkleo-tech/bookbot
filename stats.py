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

def char_counter():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    dict = {}
    for i in text:
        lower = i.lower()
        if lower not in dict:
            dict[lower] = 1
        else:
            dict[lower] += 1
    return dict

def value_pair():
    list = []
    dict = char_counter()
    for key, value in dict.items():
        if key not in list:
            list.append({key: value})
    print(list)

value_pair()