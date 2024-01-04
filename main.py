def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)

    # print(text)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(text)} words found in the document\n")

    letters = count_letters(text)
    letters_list = list(letters)
    letters_list.sort()

    for letter in letters_list:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letters[letter]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()

    return len(words)

def count_letters(text):
    letter_dict = {}

    for letter in text:
        low_letter = letter.lower()

        if low_letter in letter_dict:
            letter_dict[low_letter]+=1

        else: 
            letter_dict[low_letter] = 1

    return letter_dict

main()