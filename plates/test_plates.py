
from plates import is_valid

def test_length():
    assert is_valid('a') == False
    assert is_valid('aim2pls') == False
    assert is_valid('fat23') == True

def test_startLetters():
    assert is_valid('abs') == True
    assert is_valid('ace3b') == False
    assert is_valid('b4') == False

def test_numbersLast():
    assert is_valid('pe0ple') == False
    assert is_valid('me2') == True
    assert is_valid('fas001') == False
    assert is_valid('fas100') == True

def test_invalidChar():
    assert is_valid('for8.1') == False
    assert is_valid('g@t') == False
    assert is_valid('wall#e') == False

