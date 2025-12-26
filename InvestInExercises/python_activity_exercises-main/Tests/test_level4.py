from __future__ import division

import unittest

from level4 import solution


class Level4TestCase(unittest.TestCase):

    def test_level4_collections(self):
        validation = str(4 // 3) + '\n' + str(4 / 3)

        self.assertEqual(str(solution(4, 3)), validation)


if __name__ == '__main__':
    unittest.main()
