def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def sort_on(dict):
    return dict["num"]

def sort_char_dict(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # skip non-alphabet characters
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
