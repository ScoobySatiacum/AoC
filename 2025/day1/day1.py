def move_dial_right(steps, position):
    zero_clicks = 0
    for i in range(steps):
        position += 1
        if position > 99:
            position = 0
        if position == 0 and i != steps - 1:
            zero_clicks += 1

    return position, zero_clicks

def move_dial_left(steps, position):    
    zero_clicks = 0
    for i in range(steps):
        position -= 1
        if position == 0 and i != steps - 1:
            zero_clicks += 1
        if position < 0:
            position = 99

    return position, zero_clicks

if __name__ == "__main__":

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day1\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    position = 50

    answer = 0

    for direction in inputs:
        if direction.startswith('L'):
            steps = int(direction.replace('L', ''))
            position, zero_clicks = move_dial_left(steps, position)
            answer += zero_clicks
        else:
            steps = int(direction.replace('R', ''))
            position, zero_clicks = move_dial_right(steps, position)
            answer += zero_clicks
        if position == 0:
            answer += 1
        print(position)

    print(answer)