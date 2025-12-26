from __future__ import division

import unittest

from level6 import is_leap


class Level6TestCase(unittest.TestCase):

    # Divisible by 4 but not by 100: These are standard leap years.
    def test_level6_2024(self):
        self.assertEqual(is_leap(2024), True)

    def test_level6_2028(self):
        self.assertEqual(is_leap(2028), True)

    # Divisible by 100 but not by 400: These are common years, despite being divisible by 4.
    def test_level6_1900(self):
        self.assertEqual(is_leap(1900), False)

    def test_level6_2100(self):
        self.assertEqual(is_leap(2100), False)

    # Divisible by 400: These are leap years, even though they are also divisible by 100.
    def test_level6_2000(self):
        self.assertEqual(is_leap(2000), True)

    def test_level6_2400(self):
        self.assertEqual(is_leap(2400), True)

    # Not divisible by 4: These are common years.
    def test_level6_2019(self):
        self.assertEqual(is_leap(2019), False)

    def test_level6_2021(self):
        self.assertEqual(is_leap(2021), False)

    # Boundary values: It's important to test the boundaries around known leap years.
    def test_level6_2003(self):
        self.assertEqual(is_leap(2003), False)

    def test_level6_2005(self):
        self.assertEqual(is_leap(2005), False)

    def test_level6_2023(self):
        self.assertEqual(is_leap(2023), False)

    def test_level6_2025(self):
        self.assertEqual(is_leap(2025), False)

    # Historical dates and far future: To check the robustness for any calendar adjustments or potential usage scenarios.
    def test_level6_1700(self):
        self.assertEqual(is_leap(1700), False)

    def test_level6_2500(self):
        self.assertEqual(is_leap(2500), False)

    def test_level6_2600(self):
        self.assertEqual(is_leap(2600), False)

    # Very large numbers: To test the performance and handling of large year values.
    def test_level6_10000(self):
        self.assertEqual(is_leap(10000), True)

    def test_level6_100000(self):
        self.assertEqual(is_leap(100000), True)

    # Boundary values: It's important to test the boundaries around known leap years.
    def test_level6_negative100(self):
        self.assertEqual(is_leap(-100), False)

    def test_level6_negative400(self):
        self.assertEqual(is_leap(-400), False)

    def test_level6_3345(self):
        self.assertEqual(is_leap(3345), False)

    def test_level6_0(self):
        self.assertEqual(is_leap(0), False)


if __name__ == '__main__':
    unittest.main()
