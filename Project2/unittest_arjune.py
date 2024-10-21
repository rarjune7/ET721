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



""" Documentations:



1.Error Encountered:
   - I ran into an error when player 'O' tried to drop a chip in column 3 after player 'X'. The spot was already filled with 'X', which caused my test to fail.

2.Problem:
   - I realized that the code for dropping the chips wasn’t working correctly. It wasn’t switching players properly after each drop, so the same player could drop multiple chips in a row.

How I Fixed It duh loll 

1.Updated the `drop_chip` Method:
   - I changed the method to ensure it finds the next empty spot in the column. After placing a chip, it now correctly switches to the other player.

2.Adjusted the Test Case:
   - I reviewed the test case to make sure it checks for chips in the right spots after each drop. I also fixed the column indexes to align with how Python counts (starting from 0).

Final Code

Now, the final code combines the `Connect4` class and the test cases. It should work correctly, allowing players to take turns and drop chips in the right places.

With these changes, I feel confident that the game will run smoothly and pass all the tests!

 """