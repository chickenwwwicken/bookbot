def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_dicts = get_list_dicts(chars_dict)
#    sorted_list = get_sort_list(list_dicts)

    print(list_dicts)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    low_caps = text.lower()
    char_counts = {}
    for char in low_caps:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts


def get_list_dicts(chars_dict):
    lista = []

    for item in chars_dict:
        single_dict = {}
        count = chars_dict[item]
        single_dict[item] = count
        lista.append(single_dict)    
    return lista


def sort_on(sorted_list):
    return sorted_list['num']

'''
def get_sort_list(list_dicts):
    sorted_list = []
    for char in list_dicts:
        sorted_list.append({'char': char, 'num': list_dicts[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

''

def get_book_text(path):
    with open(path) as f:
        return f.read() 


main()
