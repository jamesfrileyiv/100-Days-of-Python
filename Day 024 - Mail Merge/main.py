NAMES_PATH = "./Input/Names/invited_names.txt"
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"
OUTPUT_PATH_ROOT = "./Output/ReadyToSend/"
PLACE_HOLDER = "[name]"


def main():
    with open(STARTING_LETTER_PATH) as letter:
        letter_template = letter.read()
    with open(NAMES_PATH) as name_file:
        for name in name_file:
            name = name.strip()
            letter = letter_template.replace(PLACE_HOLDER, name)
            output_path = f"{OUTPUT_PATH_ROOT}letter_to_{name}.txt"
            with open(output_path, mode="w") as output_file:
                output_file.write(letter)


if __name__ == "__main__":
    main()
