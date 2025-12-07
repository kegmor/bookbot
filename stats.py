def get_num_words(filename):
    word_counts = 0
    with open(filename, 'r') as f:
        for line in f:
            word_counts += len(line.split())
    return word_counts

def get_num_chars(filename):
    char_counts = {}
    with open(filename, 'r') as f:
        for line in f:
            for char in line.lower():
                if char.isalpha():
                    if char not in char_counts:
                        char_counts[char] = 1
                    else:
                        char_counts[char] += 1
    return char_counts

def create_list_num_chars(filename):
    char_dict = get_num_chars(filename)
    res = []
    for k, v in char_dict.items():
        res.append({"char": k, "num": v})
    res.sort(reverse=True, key=sort_on)
    return res


def sort_on(items):
    return items["num"]