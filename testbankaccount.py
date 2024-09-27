"""
Ravindra Arjune 
Sep 27, 2024
Test Bank Account Lab Exercise: 

"""

import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Create an instance of BankAccount with owner 'Ravi' and a starting balance of 100
        self.account = BankAccount(owner="Ravi", balance=100)

    def test_initial_balance(self):
        # Test that the account is initialized with the correct balance
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        # Test that depositing money correctly updates the balance
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        # Test that withdrawing money correctly updates the balance
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_more_than_balance(self):
        # Test that withdrawing more than the balance raises an exception
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_sequence_of_transactions(self):
        # Test a sequence of deposits and withdrawals
        self.account.deposit(50)   # Balance should be 150
        self.account.withdraw(20)  # Balance should be 130
        self.account.deposit(30)   # Balance should be 160
        self.assertEqual(self.account.get_balance(), 160)

    def test_negative_deposit(self):
        # Test that depositing a negative amount raises an exception
        with self.assertRaises(ValueError):
            self.account.deposit(-50)

    def test_negative_withdraw(self):
        # Test that withdrawing a negative amount raises an exception
        with self.assertRaises(ValueError):
            self.account.withdraw(-30)

if __name__ == "__main__":
    unittest.main()
