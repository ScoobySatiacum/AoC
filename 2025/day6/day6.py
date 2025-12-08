def part1(inputs):
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

def parse_cephalaproblems(inputs):
    data = []
    for row in inputs:
        temp = list(row)
        data.append(temp)

    operators = data[-1]
    boundries = [i - 1 for i in range(len(operators)) if operators[i] != ' ']

    problems = []

    for i in range(len(boundries)):
        cephalaproblems = []
        for row in data:
            if i < len(boundries) - 1:
                start, stop = boundries[i] + 1, boundries[i + 1]
            else:
                start, stop = boundries[i] + 1, len(row)
            new_row = []
            for j in range(start, stop):
                new_row.append(row[j])
            cephalaproblems.append(new_row)
        problems.append(cephalaproblems)

    return problems

def part2(inputs):

    problems = parse_cephalaproblems(inputs)

    answer = 0 

    for problem in problems:
        operator = problem[-1][0]
        nums = problem[:-1]
        new_nums = []
        for j in range(len(nums[0]) - 1, -1, -1):
            curr_num = ''
            for i in range(len(nums)):
                if nums[i][j] != ' ':
                    curr_num += nums[i][j]
            new_nums.append(int(curr_num))
        if operator == '+':
            answer += sum(new_nums)
        else:
            curr_answer = new_nums[0]
            for num in new_nums[1:]:
                curr_answer = curr_answer * num
            answer += curr_answer

    print(answer)

if __name__ == '__main__':

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day6\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]


    part1(inputs)
    part2(inputs)