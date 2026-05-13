import pytest 
import fuel

def test_guage():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(50) == "50%"

def test_fraction():
    assert fuel.convert("1/4") == 25

