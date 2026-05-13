import pytest 
import plates

def test_length():
    assert plates.is_valid("XBDDBHCUD13") == False
    assert plates.is_valid("X") == False

def test_alnum():
    assert plates.is_valid(":::::") == False

def test_first_two():
    assert plates.is_valid("12ABC") == False

def test_no_middle_numbers():
    assert plates.is_valid("AB12CD") == False
