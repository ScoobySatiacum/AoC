def open_input_text_file(input_path):
    input_data = []

    with open(input_path, "r", encoding="utf-8") as fo:
        input_data = [f.strip() for f in fo.readlines()]

    return input_data

def expand_input_data(input_data, expansion_times = 100):
    data = []
    for line in input_data:
        new_line = ""
        for i in range(expansion_times):
            new_line += line
        data.append(new_line)
    
    return data

def part_1(data):
    # traverse the data (trees)
    x, y = 0, 0
    movement = (-1, 3)
    tree_count = 0

    for line in data:
        if line[y] == "#":
            tree_count += 1
        x += 1
        y += 3

    return tree_count

def part_2(data):
    instructions = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    tree_counts = []

    for instruction in instructions:
        # traverse the data (trees)
        x, y = 0, 0
        movement = instruction
        tree_count = 0

        for i in range(0, len(data), movement[1]):
            line = data[i]
            if line[y] == "#":
                tree_count += 1
            x += movement[1]
            y += movement[0]

        tree_counts.append(tree_count)

    answer = tree_counts[0]
    for i in range(1, len(tree_counts)):
        answer = answer * tree_counts[i]

    return answer

if __name__ == "__main__":
    input_path = r"C:\Users\skyle\Documents\dev\AoC\2020\day3\input.txt"

    input_data = open_input_text_file(input_path)

    # expand input_data to the right ten times
    data = expand_input_data(input_data)

    part_1_answer = part_1(data)

    part_2_answer = part_2(data)

    print(part_2_answer)