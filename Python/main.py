import pytest


def to_roman(number):
    number_to_roman = {
        1: 'I',
        5: 'V',
        10: 'X'
    }
    if number <= 3:
        return number_to_roman[1] * number
    if number > 10:
        return number_to_roman[10] * int(number / 10)

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


def test_numeral_twenty_produces_XX():
    assert to_roman(20) == "XX"


def test_numeral_thirty_produces_XXX():
    assert to_roman(30) == "XXX"


if __name__ == "__main__":
    pytest.main()