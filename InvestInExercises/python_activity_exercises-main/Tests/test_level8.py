import unittest

from level8 import solution


class Level8TestCase(unittest.TestCase):

    def test_level7(self):
        self.assertEqual(solution([2, 3, 6, 6, 5]), 5)

    def test_all_same(self):
        self.assertEqual(solution([1, 1, 1, 1]), "Not enough participants with different scores")

    def test_two_elements(self):
        self.assertEqual(solution([10, 9]), 9)

    def test_negative_numbers(self):
        self.assertEqual(solution([-1, -2, -3, -4]), -2)

    def test_large_numbers(self):
        self.assertEqual(solution([1000, 999, 998, 1000]), 999)

    def test_with_zero(self):
        self.assertEqual(solution([0, 1, 0]), 0)

    def test_single_element(self):
        self.assertEqual(solution([5]), "Not enough participants with different scores")

    def test_empty_list(self):
        self.assertEqual(solution([]), "Not enough participants with different scores")

    def test_mixed_values(self):
        self.assertEqual(solution([5, 5, 5, 6, 6]), 5)


if __name__ == '__main__':
    unittest.main()
