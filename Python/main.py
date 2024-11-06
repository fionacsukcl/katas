import pytest

def to_roman(number):
    number_to_roman = {
        1: 'I',
        5: 'V',
    }
    return number_to_roman[number]

def test_numeral_one_produces_I():
    assert to_roman(1) == "I"


def test_numeral_five_produces_V():
    assert to_roman(5) == "V"


if __name__ == "__main__":
    pytest.main()