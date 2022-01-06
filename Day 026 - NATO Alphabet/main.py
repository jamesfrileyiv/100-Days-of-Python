import csv

FILE = "nato_phonetic_alphabet.csv"


def main():
    nato_alphabet = load_nato_alphabet(FILE)
    word = get_word_from_user()
    if is_valid_word(word):
        phonetic_spelling = get_nato_phonetic_spelling(word, nato_alphabet)
        print_phonetic_spelling(phonetic_spelling)
    else:
        print("Error: Invalid word entered.")
        print("Word cannot contain digits, spaces, or special characters.")
        exit(1)
    exit(0)


def load_nato_alphabet(file):
    # nato_alphabet = {}
    with open(file) as f:
        reader = csv.reader(f)
        nato_alphabet = {rows[0]: rows[1] for rows in reader}
    return nato_alphabet


def get_word_from_user():
    return input("Please enter a word: ")


def is_valid_word(word):
    if word.isalpha():
        return True
    else:
        return False


def get_nato_phonetic_spelling(word, nato_alphabet):
    return [nato_alphabet.get(char.upper()) for char in word]


def print_phonetic_spelling(phonetic):
    for word in phonetic:
        print(word, end=" ")


if __name__ == "__main__":
    main()
