if __name__ == '__main__':

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day6\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    data = []
    for row in inputs:
        new_row = [i for i in row.split(' ') if i != '']
        data.append(new_row)

    answers = []

    for i in range(len(data[0])):
        operation = data[-1][i]
        nums = []
        for item in data[:-1]:
            nums.append(int(item[i]))
        if operation == '*':
            answer = nums[0]
            for num in nums[1:]:
                answer = answer * num
            answers.append(answer)
        else:
            answers.append(sum(nums))

    print(sum(answers))