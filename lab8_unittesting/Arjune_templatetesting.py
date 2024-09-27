""" 
Ravindra Arjune 
September 27,2024
Unit Testing

"""

import unittest

def addtwonumbers(a,b):
    return a+b

#Create a unit test to check if function 'addtwonumbers' is working properly
class TestAddFunction(unittest.TestCase):
    def test_addtwonumbers(self):
        self.assertEqual(addtwonumbers(3,5),8)