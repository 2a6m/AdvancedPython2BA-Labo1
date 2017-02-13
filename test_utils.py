# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(3), 6)
        with self.assertRaises(ValueError):
            utils.fact(-5)
            utils.fact('blabla')
    
    def test_roots(self):
        self.assertEqual(utils.roots(0, 1, 0), (0))
        self.assertEqual(utils.roots(0, 0, 0), (0))
        self.assertEqual(utils.roots(4, 7, 3), (-1, -0.75))
    
    def test_integrate(self):
        self.assertEqual(utils.integrate('x', 0, 1), 0.5)
        self.assertEqual(utils.integrate('1', 0, 1), 1)
        self.assertEqual(utils.integrate('x', -1, 1), 0)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())