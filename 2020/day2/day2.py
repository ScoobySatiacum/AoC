def part_1(input_data):
    # parse the input data
    correct_passwords = []
    incorrect_passwords = []
    for item in input_data:
        instructions, password = item.split(":")
        password = password.strip()
        frequency, letter = instructions.split(" ")
        min_frequency, max_frequency = frequency.split("-")
        letter_count = int(password.count(letter))
        if letter_count >= int(min_frequency) and letter_count <= int(max_frequency):
            correct_passwords.append(password)
        else:
            incorrect_passwords.append(password)

    return len(correct_passwords)

def part_2(input_data):
    # parse the input data
    correct_passwords = []
    incorrect_passwords = []
    for item in input_data:
        instructions, password = item.split(":")
        password = password.strip()
        frequency, letter = instructions.split(" ")
        frequency_split = frequency.split("-")
        first_position = int(frequency_split[0]) - 1
        second_position = int(frequency_split[1]) - 1

        if password[first_position] == letter:
            if password[second_position] != letter:
                correct_passwords.append(password)
            else:
                incorrect_passwords.append(password)
        elif password[second_position] == letter:
            if password[first_position] != letter:
                correct_passwords.append(password)
            else:
                incorrect_passwords.append(password)
        else:
            incorrect_passwords.append(password)

    return len(correct_passwords)

if __name__ == "__main__":
    input_path = r"C:\Users\skyle\Documents\dev\AoC\2020\day2\input.txt"

    input_data = []

    with open(input_path, "r", encoding="utf-8") as fo:
        input_data = [f.strip() for f in fo.readlines()]

    print(part_1(input_data))
    print(part_2(input_data))