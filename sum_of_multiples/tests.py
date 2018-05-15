import unittest
from sum_of_multiples.sum_of_multiples import sum_of_multiples


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
