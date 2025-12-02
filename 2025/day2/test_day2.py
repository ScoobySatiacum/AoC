import pytest

from day2 import validate_ids

def test_first_range():

    sut = [str(i) for i in range(1188511880, 1188511891)]

    valid_ids = validate_ids(sut)

    assert len(valid_ids) == 1
            