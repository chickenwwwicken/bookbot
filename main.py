def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_dicts = get_list_dicts(chars_dict)
    sorted_list = get_sort_list(chars_dict)

    print(sorted_list) 


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


def get_count(sorted_list):
    return sorted_list['num']


def get_sort_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({'char': char, 'num': chars_dict[char]})
    sorted_list.sort(reverse=True, key=get_count)
    return sorted_list



def get_book_text(path):
    with open(path) as f:
        return f.read() 


main()
