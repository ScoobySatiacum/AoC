import itertools

def calculate_joltage(bank):
    bank_list = list(bank)
    joltages = []
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            num = bank[i] + bank[j]
            if num not in joltages:
                joltages.append(num)
    joltages = list(map(int, joltages))
    return max(joltages)

def calculate_joltage_varied_length(input_data):
    volts = []
    
    for banks in input_data:
        starting_pos = 0
        search_range = -11
        values = []
        
        while search_range <= 0:
            corpus = banks[starting_pos:search_range]
            if search_range == 0:
                corpus = banks[starting_pos:]
            high_val = max(i for i in corpus)
            values.append(high_val)
            starting_pos += corpus.index(str(high_val)) + 1
            search_range +=1

        volts.append(''.join(values))
    print(sum([int(i) for i in volts]))

if __name__ == '__main__':

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day3\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    jolts = []

    for bank in inputs:
        jolts.append(calculate_joltage(bank))
    print(sum(jolts))

    jolts = []
    calculate_joltage_varied_length(inputs)
    print(sum(jolts))