def part_1(inputs):
    left_side, right_side = [], []

    for item in inputs:
        nums = item.split('  ')
        left_side.append(int(nums[0]))
        right_side.append(int(nums[1].strip()))

    left_side.sort()
    right_side.sort()

    distances = []
    for i in range(len(left_side)):
        distance = abs(left_side[i] - right_side[i])
        distances.append(distance)

    return sum(distances)

def part_2(inputs):
    left_side, right_side = [], []

    for item in inputs:
        nums = item.split('  ')
        left_side.append(int(nums[0]))
        right_side.append(int(nums[1].strip()))

    similarity_score = 0
    for item in left_side:
        similarity_score += item * right_side.count(item)

    return similarity_score


if __name__ == '__main__':

    inputs_path = r"C:\Users\skyle\Documents\dev\AoC\2024\day1\input.txt"

    inputs = []
    with open(inputs_path, 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    print(part_1(inputs))
    print(part_2(inputs))