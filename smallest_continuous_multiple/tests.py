import unittest
from smallest_continuous_multiple import smallest_continuous_multiple


class TestSmallestContinuousMultiple(unittest.TestCase):

    def test_input_zero(self):
        self.assertEqual(smallest_continuous_multiple(0), 0)

    def test_input_one(self):
        self.assertEqual(smallest_continuous_multiple(1), 1)

    def test_input_two(self):
        self.assertEqual(smallest_continuous_multiple(2), 2)

    def test_input_ten(self):
        self.assertEqual(smallest_continuous_multiple(10), 2520)

    def test_input_twenty(self):
        self.assertEqual(smallest_continuous_multiple(20), 232792560)


if __name__ == '__main__':
    unittest.main()
