from my_project.calculator import Calculator
import pytest

@pytest.fixture
def calculation():
    return Calculator(10, 5)

def test_addiction(calculation):
    assert calculation.addition() == 13, "the sum is wrong"

def test_subtraction(calculation):
    assert calculation.subtraction() == 5, "the subtraction is wrong"

def test_multiplication(calculation):
    assert calculation.multiplication() == 50, "the multiplication is wrong"

def test_addiction(calculation):
    assert calculation.division() == 2.00, "the quotient is wrong"