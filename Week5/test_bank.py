import pytest
import bank

def test_h():
    assert bank.value("hi") == f"$20"
def test_hello():
    assert bank.value("hello") == f"$0"
def test_nothing():
    assert bank.value("what") == f"$100"

