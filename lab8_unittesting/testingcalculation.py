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

        #division by zero 
        def test_dividebyzero(self):
            self.assertIsNone(calculation.dividetwonumbers(10,0))

        #non-numeric testing
        def test_nonnumericvalues(self):
            self.assertIsNone(calculation.dividetwonumbers("p",2))
            self.assertIsNone(calculation.dividetwonumbers(10,"n"))

        #any another exceptions
        def test_unexpected_exception(self):
            #flag raises if 'Exception' is detected
            with self.assertRaises(Exception):
                calculation.dividetwonumbers()





if __name__ == "__main__":
    unittest.main()

