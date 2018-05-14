import unittest
from sum_of_multiples import sum_of_multiples
from helper_functions import greatest_common_divisor, least_common_multiple


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


class TestLeastCommonMultiple(unittest.TestCase):

    def test_regular(self):
        self.assertEqual(least_common_multiple(4, 3), 12)

    def test_input_is_return(self):
        self.assertEqual(least_common_multiple(15, 3), 15)

    def test_same_input(self):
        self.assertEqual(least_common_multiple(15, 15), 15)

    def test_one_prime(self):
        self.assertEqual(greatest_common_divisor(11, 4), 1)

    def test_two_primes(self):
        self.assertEqual(greatest_common_divisor(11, 7), 1)

    def test_input_one(self):
        self.assertEqual(greatest_common_divisor(11, 1), 1)


class TestSumOfMultiples(unittest.TestCase):
    
    def test_string_input(self):
        self.assertRaises(TypeError, sum_of_multiples, "string", "string", "string")

    def test_none_input(self):
        self.assertRaises(TypeError, sum_of_multiples, None, None, None)

    def test_float_input(self):
        self.assertRaises(TypeError, sum_of_multiples, 3.1415, 3.1415, 3.1415)

    def test_bool_input(self):
        self.assertRaises(TypeError, sum_of_multiples, True, True, True)

    def test_negative_input(self):
        self.assertRaises(ValueError, sum_of_multiples, 120, -10, -10)

    def test_zero_input(self):
        self.assertRaises(ValueError, sum_of_multiples, 345, 4, 0)
        
    def test_one(self):
        self.assertEqual(sum_of_multiples(1000, 3, 5), 234168)

    def test_two(self):
        self.assertEqual(sum_of_multiples(20, 4, 5), 90)

    def test_same_input(self):
        self.assertEqual(sum_of_multiples(20, 5, 5), 50)

    def test_one_unused_input(self):
        self.assertEqual(sum_of_multiples(20, 5, 25), 50)

    def test_zero_sum(self):
        self.assertEqual(sum_of_multiples(20, 30, 25), 0)


if __name__ == '__main__':
    unittest.main()
