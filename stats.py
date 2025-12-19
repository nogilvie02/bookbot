def get_num_words(book):
    count = 0
    words = book.split()
    for word in words:
        count += 1
    return count

def get_chars_dict(book):
    lowercase_book = book.lower()
    char_dict = {}
    for char in lowercase_book:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_num_chars(chars):
    counts = []
    # Create the list of dictionaries
    for char in chars:
        if char.isalpha():
            counts.append({"char": char, "num": chars[char]})
    counts.sort(reverse=True, key=sort_on)
    return counts

def sort_on(items):
    return items["num"]