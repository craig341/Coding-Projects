import unittest

from level3 import mult
from level3 import sub
from level3 import sum


class Level3TestCase(unittest.TestCase):

    def test_level3_addition1(self):
        self.assertEqual(sum(3, 5), 8)

    def test_level3_subtraction1(self):
        self.assertEqual(sub(3, 5), -2)

    def test_level3_multiplication1(self):
        self.assertEqual(mult(3, 5), 15)

    def test_level3_sumoutofbounds(self):
        self.assertEqual(sum(10000000001, 1), None)

    def test_level3_suboutofbounds(self):
        self.assertEqual(sub(10000000001, 1), None)

    def test_level3_multoutofbounds(self):
        self.assertEqual(mult(3, 10000000001), None)


if __name__ == '__main__':
    unittest.main()
