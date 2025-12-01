import pytest

from day1 import move_dial_left, move_dial_right

def test_move_dial_left_one_digit():

    position = 50

    steps = 4

    position = move_dial_left(steps, position)

    assert position == 46

def test_move_dial_left_two_digit_less_than_fifty():

    position = 50

    steps = 45

    position = move_dial_left(steps, position)

    assert position == 5

def test_move_dial_left_two_digit_more_than_fifty():

    position = 50

    steps = 99

    position = move_dial_left(steps, position)

    assert position == 51

def test_move_dial_left_three_digits():

    position = 50

    steps = 638

    position = move_dial_left(steps, position)

    assert position == 12

def test_move_dial_right_one_digit():

    position = 50

    steps = 4

    position = move_dial_right(steps, position)

    assert position == 54

def test_move_dial_right_two_digit_less_than_fifty():

    position = 50

    steps = 45

    position = move_dial_right(steps, position)

    assert position == 95

def test_move_dial_right_two_digit_more_than_fifty():

    position = 50

    steps = 99

    position = move_dial_right(steps, position)

    assert position == 49

def test_move_dial_right_three_digits():

    position = 50

    steps = 779

    position = move_dial_right(steps, position)

    assert position == 29