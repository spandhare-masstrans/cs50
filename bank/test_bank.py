import pytest
from bank import value

def test_incorrect_values():
	assert value("goodbye") == 100
	assert value("greetings") == 100

def test_case_insensitivity():
	assert value("hello") == 0
	assert value("HELLO") == 0
	assert value("hEllo") == 0

def test_partial():
	assert value("hey") == 20
	assert value("Hola") == 20

