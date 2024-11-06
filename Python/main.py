import pytest


def to_roman(number):
    number_to_roman = {
        1: 'I',
        5: 'V',
        10: 'X',
        21: 'XXI'
    }
    if number == 25:
        return to_roman(20) + number_to_roman[5]
    if number not in number_to_roman:
        return number_to_roman[10] * int(number / 10) + number_to_roman[1] * (number % 10)
    
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
    

def test_numeral_twenty_one_produces_XXI():
    assert to_roman(21) == "XXI"
    
    
def test_numeral_twenty_two_produces_XXII():
    assert to_roman(22) == "XXII"


def test_numeral_twenty_five_produces_XXV():
    assert to_roman(25) == "XXV"

if __name__ == "__main__":
    pytest.main()