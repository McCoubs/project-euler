import unittest
from sum_square_difference import sum_square_difference


class TestSumOfMultiples(unittest.TestCase):

    def test_string_input(self):
        self.assertRaises(TypeError, sum_square_difference, "string")

    def test_none_input(self):
        self.assertRaises(TypeError, sum_square_difference, None)

    def test_float_input(self):
        self.assertRaises(TypeError, sum_square_difference, 3.1415)

    def test_bool_input(self):
        self.assertRaises(TypeError, sum_square_difference, True)

    def test_negative_input(self):
        self.assertRaises(ValueError, sum_square_difference, -10)

    def test_zero_sum(self):
        self.assertEqual(sum_square_difference(0), 0)

    def test_ten(self):
        self.assertEqual(sum_square_difference(10), 2640)

    def test_ten(self):
        self.assertEqual(sum_square_difference(100), 25164150)


if __name__ == '__main__':
    unittest.main()
