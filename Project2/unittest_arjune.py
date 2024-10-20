""" 
Ravindra Arjune 

Instruction: 
test drop chip success: place the ship in the right column

"""

import unittest

class Connect4:
    def __init__(self):
        # Initialize a 6x7 board
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'  # Start with player X

    def drop_chip(self, column):
        if column < 0 or column >= 7:
            return False  # Invalid column
        # Find the lowest available row in the column
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                # Switch players
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                return True
        return False  # Column is full

class TestConnect4(unittest.TestCase):
    
    def setUp(self):
        """Create a new game before each test."""
        self.game = Connect4()
    
    def test_drop_chip_success(self):
        """Test that a chip is successfully dropped into the correct column."""
        
        # Player X drops a chip in column 3
        success = self.game.drop_chip(3)
        self.assertTrue(success, "Chip should be dropped successfully.")
        self.assertEqual(self.game.board[5][3], 'X', "Chip should be at the lowest space in column 3.")
        
        # Player O drops a chip in column 3
        success = self.game.drop_chip(3)
        self.assertTrue(success, "Chip should be dropped successfully.")
        self.assertEqual(self.game.board[4][3], 'O', "Chip should be in the next space in column 3.")
        
        # Player X drops a chip in column 5
        success = self.game.drop_chip(5)
        self.assertTrue(success, "Chip should be dropped successfully.")
        self.assertEqual(self.game.board[5][5], 'X', "Chip should be at the lowest space in column 5.")

if __name__ == '__main__':
    unittest.main()
