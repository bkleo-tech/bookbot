#Hello project #1,change path

def word_counter(text):
    words = text.split()
    word_count = len(words)
    return word_count

def char_counter(text):
    dict = {}
    for i in text:
        lower = i.lower()
        if lower not in dict:
            dict[lower] = 1
        else:
            dict[lower] += 1
    return(dict)
    

def sort_list(text):
    list = []
    for key, value in text.items():
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
