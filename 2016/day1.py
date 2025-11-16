if __name__ == "__main__":
    directions = []
    with open(r"C:\Users\skyle\Documents\dev\AoC\2016\day1_input.txt") as fo:
        temp = fo.read()
        directions = temp.split(", ")
    
    facing_directions = {
        "N": (0, -1), "E": (1, 0), "S":(0, 1), "W": (-1, 0)
    }
    current_direction = 0
    coords = (0, 0)
    for direction in directions:
        split_direction = list(direction)
        if split_direction[0] == "L":
            current_direction -= 1
        else:
            current_direction += 1
        dire
        
