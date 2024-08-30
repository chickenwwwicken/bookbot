def main():

    book_path = 'books/frankenstein.txt'
    
    # full text 
    text = get_book_text(book_path)
    
    # number of words in the text
    num_words = get_num_words(text)
    
    # dictionary of all the characters and their count in the text
    chars_dict = get_chars_dict(text)

    # list with all the {character:count}'s as dictionaries
    list_dicts = get_list_dicts(chars_dict)

    # sorted list of all character:count's ordered from most appearances to least
    sorted_list = get_sort_list(chars_dict)


    # Printed book report
    print(f'--- Begin report of {book_path} ---')
    print('-------     by bookbot      -------')

    for item in sorted_list:
        
        # printint all letters
        if not item['char'].isalpha():
            continue
        print(f"'{item['char']}' character was found {item['num']} times")
    print("-----------------------------------")
    
    for item in sorted_list:

        # printing all extras
        if item['char'].isalpha():
            continue
        print(f"'{item['char']}' character was found {item['num']} times")
    print("-----------------------------------")

    print(f"Ammount of words in the book: {num_words}")
    
    print("-----------------------------------")
    
    print(f"--- End of book report {book_path} ---")



# split all text to find the ammount of words
def get_num_words(text):
    words = text.split()
    return len(words)


# counting how many times each letter appears in text
def get_chars_dict(text):
    low_caps = text.lower()
    char_counts = {}
    for char in low_caps:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts


# making a list of dictionaries with this format {character : count}
def get_list_dicts(chars_dict):
    lista = []

    for item in chars_dict:
        single_dict = {}
        count = chars_dict[item]
        single_dict[item] = count
        lista.append(single_dict)    
    return lista


# getting the value (count) of each character and returning it so it can be used for sorting
def get_count(sorted_list):
    return sorted_list['num']


# getting a list of dictionaries but sorted from most appearances to least 
def get_sort_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({'char': char, 'num': chars_dict[char]})
    sorted_list.sort(reverse=True, key=get_count)
    return sorted_list



# gets the book from our path in pc, opens it, and reads it
def get_book_text(path):
    with open(path) as f:
        return f.read() 


main()
