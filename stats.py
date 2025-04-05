def get_num_words(book_content):
    words = book_content.split()
    return len(words)

def get_character_count(book_content):
    char_map = {}

    for letter in book_content.lower():
        existing_count = char_map.get(letter, 0)
        char_map[letter] = existing_count + 1

    return char_map

def __sort_by_count(dict):
    return dict['count']

def get_sorted_dict(char_count):
    sorted_list = []

    for k, v in char_count.items():
        sorted_list.append({'letter': k, 'count': v})

    sorted_list.sort(reverse=True, key=__sort_by_count)
    return sorted_list
