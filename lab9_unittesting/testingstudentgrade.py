"""
Ravindra Arjune
Sep 30, unit testing 'input' data
"""

import unittest
from unittest.mock import patch
import io
import studentgrade 

class TestManFunction(unittest.TestCase):
    #TEST WITH VALID INPUTS
    @patch('builtins.input', side_effects = ['3', '85', '90', '75'])
    @patch('sys.stdout', new_callable = io.StringIO)

    def test_valid_input(self, mock_stdout, mock_input):
        # call the function 'main()' from 'studentgrade.py'
        studentgrade.main()

        #retrieve the capture output
        output = mock_stdout.getvalue()

        #check if the printed output is as expected
        self.assertIn("The class average is 78.50 \n ", output)
    
    #TEST FOR INVALID INPUT

    @patch('builtins.input', side_effects = ['-1', '2', '85','72'])
    @patch('sys.stdout', new_callable = io.StringIO)

    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        # call the function 'main()' from 'studentgrade.py'
        studentgrade.main()

        #retrieve the capture output
        output = mock_stdout.getvalue()

        #check if the printed output is as expected
        self.assertIn("Invalid input.  \n", output)
        self.assertIn("The class average is 78.50", output)

        # TEST FOR INVALID INPUT GRADE
        @patch('builtins.input', side_effects = ['2', '105','82', '-10', '70'])
        @patch('sys.stdout', new_callable = io.StringIO)

        def test_invalid_grade(self, mock_stdout, mock_input):
            #call the function 'main()' from 'studentgrade.py'
            studentgrade.main()

            #  retreive the capture output
            output = mock_stdout.getvalue()

            # check if the printed output is as expected
            self.assertIn("Grade must be between 0 and 100. ", output)

            self.assertIn("The class average is 76.00", output)

        #TEST FOR INVALID VALUE OF INPUT NUMBER OF STUDENTS

        @patch('builtins.input', side_effect=['0', '3', '90', '80', '70'])
        @patch('sys.stdout', new_callable=io.StringIO)

        def test_invalid_number_of_students(self, mock_stdout, mock_input):
            # call the function 'main()' from 'studentgrade.py'
               studentgrade.main()

            # retrieve the captured output
        output = mock_stdout.getvalue()

        # check if the printed output is as expected
        self.assertIn("Number of students must be greater than 0.", output)


        #TEST FOR INVALID VALUE OF GRADE
        
        @patch('builtins.input', side_effect=['2', '-5', '85', '95'])
        @patch('sys.stdout', new_callable=io.StringIO)
        def test_invalid_grade_input(self, mock_stdout, mock_input):
             # call the function 'main()' from 'studentgrade.py'
               studentgrade.main()

        # retrieve the captured output
        output = mock_stdout.getvalue()

        # check if the printed output is as expected
        self.assertIn("Grade must be between 0 and 100.", output)



if __name__ == "__main__":
    unittest.main()