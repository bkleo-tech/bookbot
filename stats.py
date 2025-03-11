#Hello project #1
path = "books/frankenstein.txt"

def get_book_text(books):
    with open(books) as file:
        return file.read()

def main():
    text = get_book_text(path)
    return text

def word_counter():
    text = get_book_text(path)
    words = text.split()
    word_count = len(words)
    return word_count

def char_counter():
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
        sort_list = {"char": key, "count": value}
        if key not in list:
            list.append(sort_list)
    print(list)


def sort_list():
    list = []
    dict = char_counter()

    for key, value in dict.items():
        entry = {"char": key, "count": value}
        list.append(entry)

    # Sort this list
    list.sort(key=lambda x: x["count"], reverse=True)
    
    # Get two value-pair
    two_pair_set = []
    for i in list:
        two_pair_dict = {}
        char = i["char"]
        count = i["count"]
        two_pair_dict[char] = count
        two_pair_set.append(two_pair_dict)
    
    return two_pair_set
    print(two_pair_set)
