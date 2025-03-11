from stats import word_counter, sort_list, path

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path}...")
print("----------- Word Count ----------")
print(f"Found {word_counter()} total words")
print("--------- Character Count -------")

to_print = sort_list()
for i in to_print:
    character = list(i.keys())[0]
    if character.isalpha():
        count = i[character]
        print(f"{character}: {count}")

print("============= END ===============")