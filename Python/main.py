import pytest


def to_roman(number):
    number_to_roman = {
        1: 'I',
        5: 'V',
        10: 'X'
    }
    if number <= 3:
        return number_to_roman[1] * number
    
    return number_to_roman[number]


def test_numeral_one_produces_I():
    assert to_roman(1) == "I"


def test_numeral_five_produces_V():
    assert to_roman(5) == "V"


def test_numeral_ten_produces_X():
    assert to_roman(10) == "X"


def test_numeral_two_produces_II():
    assert to_roman(2) == "II"


def test_numeral_three_produces_III():
    assert to_roman(3) == "III"


if __name__ == "__main__":
    pytest.main()