import pytest

def to_roman(number):
    return "I"

def test_numeral_one_produces_I():
    assert to_roman(1) == "I"

if __name__ == "main":
    pytest.main()