import pytest

from day2 import validate_ids_part1

def validate_ids_part2(id_range):
    
    minimum = 1
    maximum = len(id_range[-1]) // 2
    pattern_length_options = [i for i in range(minimum, maximum + 1)]

    valid_ids = []

    for len_option in pattern_length_options:    
        for item in id_range:

            pattern_length = len_option

            pattern = item[0:pattern_length]
            content = item[pattern_length:len(item)]

            if content:
                split_content = content.split(pattern)
                test = [i for i in split_content if i != '']
                if not test:
                    if item not in valid_ids:
                        valid_ids.append(item)

    return valid_ids

def test_part1_ranges():

    sut = [str(i) for i in range(1188511880, 1188511891)]

    valid_ids = validate_ids_part1(sut)

    assert len(valid_ids) == 1

def test_part2_ranges():

    sut = [str(i) for i in range(1, 21)]

    valid_ids = validate_ids_part2(sut)

    assert len(valid_ids) == 1