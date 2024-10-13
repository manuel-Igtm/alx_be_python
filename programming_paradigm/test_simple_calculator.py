# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for the add method
    def test_addition(self):
        #Test the addition method.
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)  # Test with floats

    # Test for the subtract method
    def test_subtraction(self):
        #Test the subtraction method.
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(1.5, 0.5), 1.0)  # Test with floats

    # Test for the multiply method
    def test_multiplication(self):
        #Test the multiplication method.
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)  # Test with floats

    # Test for the divide method
    def test_division(self):
        #Test the division method.
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(1.5, 0.5), 3.0)  # Test with floats

        # Test division by zero (should return None)
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    # Additional tests for edge cases
    def test_edge_cases(self):
        #Test additional edge cases.
        # Test adding, subtracting, and multiplying large numbers
        self.assertEqual(self.calc.add(10**6, 10**6), 2 * 10**6)
        self.assertEqual(self.calc.subtract(10**6, 10**5), 9 * 10**5)
        self.assertEqual(self.calc.multiply(10**6, 10**6), 10**12)

        # Test dividing by a very small number
        self.assertAlmostEqual(self.calc.divide(1, 1e-6), 1e6)
        self.assertAlmostEqual(self.calc.divide(-1, 1e-6), -1e6)

if __name__ == "__main__":
    unittest.main()
