def open_input_text_file(input_path):
    input_data = []

    with open(input_path, "r", encoding="utf-8") as fo:
        input_data = [f.strip() for f in fo.readlines()]

    return input_data

if __name__ == "__main__":
    input_path = r"C:\Users\skyle\Documents\dev\AoC\2020\day4\input.txt"

    input_data = open_input_text_file(input_path)

    