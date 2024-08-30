def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_count = count_chars(text)
    lista_dict = list_of_dicts(dict_count)
    
    print(lista_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    low_caps = text.lower()
    char_counts = {}
    for char in low_caps:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts


def list_of_dicts(dict_count):
    lista = []

    for item in dict_count:
        single_dict = {}
        count = dict_count[item]
        single_dict[item] = count
        lista.append(single_dict)    
    return lista


def get_book_text(path):
    with open(path) as f:
        return f.read() 


main()
