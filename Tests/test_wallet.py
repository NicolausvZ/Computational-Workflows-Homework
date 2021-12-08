# test_wallet.py

import unittest
from Wallet.wallet import Wallet


class Test_Wallet(unittest.TestCase):
    def test_default_initial_amount(self):
        wallet = Wallet()
        assert wallet.balance == 0

    def test_setting_initial_amount(self):
        wallet = Wallet(100)
        assert wallet.balance == 100

    def test_wallet_add_cash(self):
        wallet = Wallet(10)
        wallet.add_cash(90)
        assert wallet.balance == 100

    def test_wallet_spend_cash(self):
        wallet = Wallet(20)
        wallet.spend_cash(10)
        assert wallet.balance == 10


if __name__ == '__main__':
    unittest.main()