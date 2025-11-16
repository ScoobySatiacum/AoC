if __name__ == "__main__":
    input_path = r"C:\Users\skyle\Documents\dev\AoC\2020\day1\input.txt"

    input_data = []

    with open(input_path, "r", encoding="utf-8") as fo:
        input_data = [int(f.strip()) for f in fo.readlines()]

    answer = None

    for i in range(len(input_data) - 2):
        for j in range(len(input_data) - 2):
            for k in range(len(input_data) - 2):
                if input_data[i] + input_data[j] + input_data[k] == 2020:
                    answer = input_data[i] * input_data[j] * input_data[k]
                    break

    print(answer)