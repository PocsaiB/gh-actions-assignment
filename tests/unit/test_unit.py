import unittest
from src.calculator import Calculator

class TestCalculatorUnit(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()