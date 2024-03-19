def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = count_characters(text)
    list_of_dict = list_of_dicts(num_letters)
    new_list_of_dict = sorted(list_of_dict, key=lambda x: x['num'], reverse=True)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print('\n')
    for letter in new_list_of_dict:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")
    
    print("--- End report  ---")
    
    
    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    frecuency = {}
    for character in text:
        if character.isalpha(): # Check if the character is a letter
            character = character.lower() # Convert the character to lowercase
            frecuency[character] = frecuency.get(character, 0) + 1
    
    return frecuency

def list_of_dicts(dict):
    list_of_dict = [{"letter": key, "num": value} for key, value in dict.items()]
    return list_of_dict
   

def sort_on(dict):
    return dict["num"]


main()