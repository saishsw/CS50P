from twttr import shorten
import pytest

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("saish") == "ssh"

def test_num():
    with pytest.raises(TypeError):
        shorten(123)
