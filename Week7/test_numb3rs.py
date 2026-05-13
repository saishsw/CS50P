import pytest 
import numb3rs

def test_validate_num():
    assert numb3rs.validate("512.512.512.512") is False
    assert numb3rs.validate("255.255.255.255") is True

def test_validate_alphabet():
        assert numb3rs.validate("abc.255.255.255") is False
