def validate_ids(id_range):

    valid_ids = []
    
    for item in id_range:
        if len(item) % 2 == 0:
            pattern_length = len(item) // 2

            pattern = item[0:pattern_length]
            content = item[pattern_length:len(item)]

            if pattern in content:
                valid_ids.append(int(item))

    return valid_ids

if __name__ == '__main__':

    inputs = []
    with open(r'C:\Users\skyle\Documents\dev\AoC\2025\day2\input.txt', 'r', encoding='utf-8') as fo:
        inputs = [r.replace("\n", "") for r in fo.readlines()]

    ranges = inputs[0].split(',')

    answers = []

    # parse ranges
    for products in ranges:
        products_split = products.split('-')
        beginning, end = int(products_split[0]), int(products_split[1])
        product_range = [str(i) for i in range(beginning, end + 1)]

        valid_ids = validate_ids(product_range)
        if valid_ids:
            answers.extend(valid_ids)

    print(sum(answers))