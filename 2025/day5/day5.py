if __name__ == '__main__':

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day5\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    fresh_ranges = [i for i in inputs if '-' in i]
    food_ids = [int(i) for i in inputs if '-' not in i and i != '']

    fresh_ranges_expanded = []
    for ranges in fresh_ranges:
        temp = ranges.split('-')
        minimum, maximum = int(temp[0]), int(temp[1])
        fresh_ranges_expanded.append((minimum, maximum))
    
    good_food = 0

    for food_id in food_ids:
        for ranges in fresh_ranges_expanded:
            if food_id > ranges[0] and food_id < ranges[-1]:
                good_food += 1
                break

    print(good_food)

    fresh_ranges_expanded.sort(key=lambda x: x[0])

    new_ranges = [fresh_ranges_expanded[0]]

    for i in range(1, len(fresh_ranges_expanded)):
        minimum, maximum = fresh_ranges_expanded[i][0], fresh_ranges_expanded[i][1]
        if minimum == maximum:
            pass
        # check if there are overlaps, if not add the range
        tests = [r for r in new_ranges if minimum - 1 <= r[1]]
        if not tests:
            new_ranges.append(fresh_ranges_expanded[i])
        else:
            for test in tests:
                if maximum > test[1]:
                    for i in range(len(new_ranges)):
                        if new_ranges[i] == test:
                            new_ranges[i] = (new_ranges[i][0], maximum)
                else:
                    pass

    good_food = 0
    for item in new_ranges:
        value = (item[1] - item[0]) + 1
        good_food += value

    print(good_food)