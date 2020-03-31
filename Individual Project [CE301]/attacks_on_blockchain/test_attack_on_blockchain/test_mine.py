import unittest
import os
import sys
from selfish_mine_simulator import Mine

class Test_Mine(unittest.TestCase):

    def setUp(self):
        self.selfish_mine_simulator = Mine()

    def test_write(self):
        test_data = self.selfish_mine_simulator.read()
        self.assertTrue(os.path.exists('../attacks_on_blockchain/results.csv'))
        self.assertIsInstance(test_data, list)
        self.assertTrue(test_data, ["function data to match here"])

    def test_main(self):



        pass

    def tearDown(self):
        del(self.selfish_mine_simulator)



