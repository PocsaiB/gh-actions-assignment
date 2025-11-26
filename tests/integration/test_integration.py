import unittest
from src.calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    def test_workflow(self):
        # Simulating a workflow using multiple methods
        calc = Calculator()
        sum_val = calc.add(2, 3)
        result = calc.multiply(sum_val, 2)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()