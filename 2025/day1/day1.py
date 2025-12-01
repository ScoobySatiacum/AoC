def move_dial_right(steps, position):
    for i in range(steps):
        position += 1
        if position > 99:
            position = 0

    return position

def move_dial_left(steps, position):    
    
    for i in range(steps):
        position -= 1
        if position < 0:
            position = 99

    return position

if __name__ == "__main__":

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day1\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    position = 50

    answer = 0

    for direction in inputs:
        if direction.startswith('L'):
            steps = int(direction.replace('L', ''))
            position = move_dial_left(steps, position)
        else:
            steps = int(direction.replace('R', ''))
            position = move_dial_right(steps, position)

        if position == 0:
            answer += 1
        print(position)

    print(answer)