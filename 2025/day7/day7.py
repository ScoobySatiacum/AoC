if __name__ == '__main__':
    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day7\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    tachyon_beams = {inputs[0].index('S'): 1}
    splits = 0
    
    for i in range(len(inputs)):
        line = inputs[i]
        for j in range(len(line)):
            if line[j] == '^':
                if j in tachyon_beams.keys():
                    splits += 1
                    if j + 1 not in tachyon_beams.keys():
                        tachyon_beams[j + 1] = 0
                    tachyon_beams[j + 1] += tachyon_beams[j]

                    if j - 1 not in tachyon_beams.keys():
                        tachyon_beams[j - 1] = 0
                    tachyon_beams[j - 1] += tachyon_beams[j]
                    del tachyon_beams[j]
    
    print(splits)
    print(sum(tachyon_beams.values()))