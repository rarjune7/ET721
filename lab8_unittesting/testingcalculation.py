"""
Ravindra Arjune
Example 2: Calculation Testing

"""

import unittest
import calculation


class TestCalcuation(unittest.TestCase):
    def test_addthreenumbers(self):
        self.assertEqual(calculation.addthreenumbers(1,2,3),6)
        self.assertEqual(calculation.addthreenumbers(5,3), 8)
        self.assertEqual(calculation.addthreenumbers(),0)

if __name__ == "__main__":
    unittest.main()

    