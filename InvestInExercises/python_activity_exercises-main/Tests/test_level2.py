import unittest

from level2 import solution


class Level2TestCase(unittest.TestCase):

    def test_level2isOdd(self):
        self.assertEqual(solution(3), 'Weird')

    def test_level2isNotOdd(self):
        self.assertEqual(solution(4), 'Not Weird')

    def test_level2isEveninRangeNotWeird(self):
        self.assertEqual(solution(2), 'Not Weird')

    def test_level2isNotEveninRangeNotWeird(self):
        self.assertEqual(solution(5), 'Weird')

    def test_level2isEveninRangeWeird(self):
        self.assertEqual(solution(8), 'Weird')

    def test_level2isNotEveninRangeWeird(self):
        self.assertEqual(solution(15), 'Weird')

    def test_level2isEveninRangeGreaterThan20(self):
        self.assertEqual(solution(22), 'Not Weird')

    def test_level2isNotEveninRangeGreaterThan20(self):
        self.assertEqual(solution(23), 'Weird')

    def test_level2isEveninRangeGreaterThan100(self):
        self.assertEqual(solution(102), None)


if __name__ == '__main__':
    unittest.main()
