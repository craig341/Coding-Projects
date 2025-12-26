import unittest

from Solutions.level7 import solution


class Level7TestCase(unittest.TestCase):

    def test_level7(self):
        self.assertEqual(solution(5), '12345')

    def test_level7_zero(self):
        self.assertEqual(solution(0), '')

    def test_level7_negative(self):
        self.assertEqual(solution(-1), '')


if __name__ == '__main__':
    unittest.main()
