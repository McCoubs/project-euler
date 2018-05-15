import unittest
from helper_functions.greatest_common_divisor import greatest_common_divisor
from helper_functions.least_common_multiple import least_common_multiple
from helper_functions.get_primes import eratosthenes_primes
from helper_functions.get_factors import get_factors


class TestGreatestCommonDivisor(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(greatest_common_divisor(20, 15), 5)

    def test_input_is_return(self):
        self.assertEqual(greatest_common_divisor(15, 3), 3)

    def test_same_input(self):
        self.assertEqual(greatest_common_divisor(15, 15), 15)

    def test_one_prime(self):
        self.assertEqual(greatest_common_divisor(11, 4), 1)

    def test_two_primes(self):
        self.assertEqual(greatest_common_divisor(11, 7), 1)

    def test_input_one(self):
        self.assertEqual(greatest_common_divisor(11, 1), 1)

    def test_input_zero(self):
        self.assertEqual(least_common_multiple(11, 0), 0)


class TestLeastCommonMultiple(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(least_common_multiple(4, 3), 12)

    def test_input_is_return(self):
        self.assertEqual(least_common_multiple(15, 3), 15)

    def test_same_input(self):
        self.assertEqual(least_common_multiple(15, 15), 15)

    def test_one_prime(self):
        self.assertEqual(least_common_multiple(11, 4), 44)

    def test_two_primes(self):
        self.assertEqual(least_common_multiple(11, 7), 77)

    def test_input_one(self):
        self.assertEqual(least_common_multiple(11, 1), 11)

    def test_input_zero(self):
        self.assertEqual(least_common_multiple(11, 0), 0)


class TestEratosthenesPrimes(unittest.TestCase):

    def test_small_prime(self):
        self.assertEqual(eratosthenes_primes(7), [2, 3, 5, 7])

    def test_large_prime(self):
        self.assertEqual(eratosthenes_primes(97), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                                                   67, 71, 73, 79, 83, 89, 97])

    def test_small_non_prime(self):
        self.assertEqual(eratosthenes_primes(12), [2, 3, 5, 7, 11])

    def test_large_non_prime(self):
        self.assertEqual(eratosthenes_primes(102), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                                                    67, 71, 73, 79, 83, 89, 97, 101])

    def test_input_zero(self):
        self.assertEqual(eratosthenes_primes(0), [])

    def test_input_one(self):
        self.assertEqual(eratosthenes_primes(1), [])

    def test_input_two(self):
        self.assertEqual(eratosthenes_primes(2), [2])


class TestGetFactors(unittest.TestCase):

    def test_small_prime(self):
        self.assertEqual(get_factors(7), {1, 7})

    def test_large_prime(self):
        self.assertEqual(get_factors(97), {1, 97})

    def test_small_non_prime(self):
        self.assertEqual(get_factors(12), {1, 2, 3, 4, 6, 12})

    def test_large_non_prime(self):
        self.assertEqual(get_factors(100), {1, 2, 4, 5, 10, 20, 25, 50, 100})

    def test_input_zero(self):
        self.assertEqual(get_factors(0), None)

    def test_input_one(self):
        self.assertEqual(get_factors(1), {1})


if __name__ == '__main__':
    unittest.main()
