import copy

def solve(inputs):

    new_inputs = copy.deepcopy(inputs)

    directions = {
        'N': (0, -1),
        'NE': (1, -1),
        'E': (1, 0),
        'SE': (1, 1),
        'S': (0, 1),
        'SW': (-1, 1),
        'W': (-1, 0),
        'NW': (-1, -1)
    }

    accessible_rolls = 0

    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            if inputs[i][j] == '@':
                roll_count = 0
                # check every direction
                for k, v in directions.items():
                    y, x = i, j
                    y, x = i + v[1], j + v[0]
                    if y > -1:
                        if x > -1:
                            try:
                                if inputs[y][x] == '@':
                                    roll_count += 1
                            except IndexError as ie:
                                pass
                if roll_count < 4:
                    accessible_rolls += 1
                    new_inputs[i][j] = '.'
    
    return accessible_rolls, new_inputs

def part2(accessible_rolls, total, inputs):
    if accessible_rolls == 0:
        return total
    else:
        accessible_rolls, inputs = solve(inputs)
        if accessible_rolls == 0:
            print(total)
            return total
        else:
            total += accessible_rolls
            part2(accessible_rolls, total, inputs)


if __name__ == '__main__':

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day4\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]
    
    inputs = [list(i) for i in inputs]
    
    #print(solve(inputs)) 
    print(part2(-1, 0, inputs))