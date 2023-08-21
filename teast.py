import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 16, 1) == 15

    def test_division(self):
         assert self.calc.division(self, 8, 2) == 4

    def test_multiply(self):
        assert self.calc.multiply(self, 8, 2) == 16

    def teardown(self):
        print('Выполнения метода Teardown')