"""
Ravindra Arjune
Example 3: verify if the email, fullname, and salary fields are correclty formatted
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    # set up of templates

    def setUp(self):
        # create an instance of the class Employee
        emp1 = Employee("Peter", "Pan", 50000)

    def test_emailemployee(self):
        self.assertEqual(self.emp1.emailemployee, "PeterPan@email.com") 

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Pan, Peter")

    def test_app_raise(self):
        self.emp1.apply_raise()

        self.assertEqual(self.emp1.apply_raise, 52500)

if __name__ == "__main__":
    unittest.main()


    