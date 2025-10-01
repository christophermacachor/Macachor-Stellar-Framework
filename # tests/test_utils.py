# tests/test_utils.py

import unittest
from src.utils import calculate_thrust

class TestUtils(unittest.TestCase):
    def test_calculate_thrust(self):
        thrust = calculate_thrust(1.0, 2.0, 3.0, 4.0, 5.0)
        self.assertAlmostEqual(thrust, expected_value)  # Replace expected_value with actual expected result

if __name__ == '__main__':
    unittest.main()
