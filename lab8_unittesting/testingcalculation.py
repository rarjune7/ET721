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
        self.assertEqual(calculation.addthreenumbers(9), 9)
        self.assertEqual(calculation.addthreenumbers(),0)

    def test_subtracttwonumbers(self):
        self.assertEqual(calculation.subtracttwonumbers(2,8), -6)
        self.assertEqual(calculation.subtracttwonumbers(8,2),6)

    def test_dividetwonumbers(self):
        self.assertEqual(calculation.dividetwonumbers(8,2),4)
        self.assertEqual(calculation.dividetwonumbers(-8,2),-4)
        # float comparison
        self.assertEqual(calculation.dividetwonumbers(7,2), 3.5)


if __name__ == "__main__":
    unittest.main()

