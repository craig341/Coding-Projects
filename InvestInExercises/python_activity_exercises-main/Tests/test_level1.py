import unittest

from level1 import solution


class Level1TestCase(unittest.TestCase):

    def test_level1(self):
        self.assertEqual(solution(), 'Hello World!')


if __name__ == '__main__':
    unittest.main()
