import unittest
from find_nth_prime.find_nth_prime import find_nth_prime


class TestFindNthPrime(unittest.TestCase):

    def test_string_input(self):
        self.assertRaises(TypeError, find_nth_prime, "string")

    def test_none_input(self):
        self.assertRaises(TypeError, find_nth_prime, None)

    def test_float_input(self):
        self.assertRaises(TypeError, find_nth_prime, 3.1415)

    def test_bool_input(self):
        self.assertRaises(TypeError, find_nth_prime, True)

    def test_negative_input(self):
        self.assertRaises(ValueError, find_nth_prime, -10)

    def test_input_zero(self):
        self.assertRaises(ValueError, find_nth_prime, 0)

    def test_input_five(self):
        self.assertEqual(find_nth_prime(5), 11)

    def test_input_one(self):
        self.assertEqual(find_nth_prime(1), 2)

    def test_large_input(self):
        self.assertEqual(find_nth_prime(100), 541)


if __name__ == '__main__':
    unittest.main()
