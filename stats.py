
def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_dict = {}
    text_lower = text.lower()
    for c in text_lower:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict

def sort_on(dict_for_sort):
    return dict_for_sort["num"]

def get_sorted_char_counts(text):
    char_count_dict = get_char_counts(text)
    
    char_dict_list = []

    for key in char_count_dict:
        if not key.isalpha():
            continue

        char_dict = {
            "char": key,
            "num": char_count_dict[key]
        }

        char_dict_list.append(char_dict)
    
    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list


