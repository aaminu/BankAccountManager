import unittest
import BankAccount


class TestAccount(unittest.TestCase):
    def test_account_creation(self):
        user = BankAccount.Account('100S234', 10000)
        self.assertEqual({'acct_num': '100S234',
                          'balance': 10000
                          }, user.__dict__)


if __name__ == '__main__':
    unittest.main()
