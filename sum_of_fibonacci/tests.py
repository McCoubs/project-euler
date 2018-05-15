import unittest
from sum_of_fibonacci.sum_of_fibonacci import sum_of_fibonacci


class TestSumOfFibonacci(unittest.TestCase):

    def test_sum_even(self):
        self.assertEqual(sum_of_fibonacci(100, True), 188)

    def test_sum_odd(self):
        self.assertEqual(sum_of_fibonacci(100, False), 187)

    def test_sum_even_two(self):
        self.assertEqual(sum_of_fibonacci(200, True), 798)

    def test_sum_odd_two(self):
        self.assertEqual(sum_of_fibonacci(200, False), 420)


if __name__ == '__main__':
    unittest.main()
