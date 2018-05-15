import unittest
from largest_prime_factor.largest_prime_factor import largest_prime_factor


class TestLargestPrimeFactor(unittest.TestCase):

    def test_input_zero(self):
        self.assertEqual(largest_prime_factor(0), None)

    def test_input_one(self):
        self.assertEqual(largest_prime_factor(1), None)

    def test_input_two(self):
        self.assertEqual(largest_prime_factor(2), 2)

    def test_input_ten(self):
        self.assertEqual(largest_prime_factor(10), 5)

    def test_input_twenty(self):
        self.assertEqual(largest_prime_factor(20), 5)

    def test_input_euler(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()
