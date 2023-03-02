#! /usr/bin/env python3
import pytest

# write a calculator class that can add, subtract, multiply, and divide
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    

# write 5 tests for each method of the calculator class, using pytest
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(5, 2) == 7
    assert calc.add(3, 4) == 7
    assert calc.add(1, 1) == 2
    assert calc.add(1, 0) == 1

def test_subtract():
    calc = Calculator()
    assert calc.subtract(1, 2) == -1
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(3, 4) == -1
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(1, 0) == 1

def test_multiply():
    calc = Calculator()
    assert calc.multiply(1, 2) == 2
    assert calc.multiply(5, 2) == 10
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(1, 1) == 1
    assert calc.multiply(1, 0) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(1, 2) == 0.5
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(3, 4) == 0.75
    assert calc.divide(1, 1) == 1
    assert calc.divide(1, 0) == 1
