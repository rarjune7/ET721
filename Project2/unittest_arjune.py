""" 
Ravindra Arjune 

Instruction: 
test drop chip success: place the ship in the right column

"""

import unittest
from main import Connect4  # Adjust the import based on your file structure

class TestConnect4(unittest.TestCase):
    
    def setUp(self):
        """Set up a new game before each test."""
        self.game = Connect4()
    
    def test_drop_chip_success(self):
        """Test that a chip is successfully dropped into the correct column."""
        # Player X drops a chip in column 3
        success = self.game.drop_chip(3)
        self.assertTrue(success, "Chip should be dropped successfully.")
        self.assertEqual(self.game.board[5][2], 'X', "Chip should be placed at the lowest available space in column 3.")
        
        # Player O drops a chip in column 3
        success = self.game.drop_chip(3)
        self.assertTrue(success, "Chip should be dropped successfully.")
        self.assertEqual(self.game.board[4][2], 'O', "Chip should be placed at the next available space in column 3.")
        
        # Player X drops a chip in column 5
        success = self.game.drop_chip(5)
        self.assertTrue(success, "Chip should be dropped successfully.")
        self.assertEqual(self.game.board[5][4], 'X', "Chip should be placed at the lowest available space in column 5.")

if __name__ == '__main__':
    unittest.main()
