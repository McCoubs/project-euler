import unittest
from pythagorean_triplets.pythagorean_triplets import pythagorean_triplets


class TestPythagoreanTriplets(unittest.TestCase):

    def test_string_input(self):
        self.assertRaises(TypeError, pythagorean_triplets, "string")

    def test_none_input(self):
        self.assertRaises(TypeError, pythagorean_triplets, None)

    def test_float_input(self):
        self.assertRaises(TypeError, pythagorean_triplets, 3.1415)

    def test_bool_input(self):
        self.assertRaises(TypeError, pythagorean_triplets, True)

    def test_negative_input(self):
        self.assertRaises(ValueError, pythagorean_triplets, -10)

    def test_input_zero(self):
        self.assertEqual(pythagorean_triplets(0), None)

    def test_input_one(self):
        self.assertEqual(pythagorean_triplets(1), None)

    def test_input_two(self):
        self.assertEqual(pythagorean_triplets(2), None)

    def test_input_three(self):
        self.assertEqual(pythagorean_triplets(3), None)

    def test_input_thousand(self):
        self.assertEqual(pythagorean_triplets(1000), {"a": 200, "b": 375, "c": 425, "abc": 31875000})


if __name__ == '__main__':
    unittest.main()
