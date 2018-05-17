import unittest
from largest_continuous_product.largest_continuous_product import largest_continuous_product


class TestLargestContinuousProduct(unittest.TestCase):
    
    def test_string_input(self):
        self.assertRaises(TypeError, largest_continuous_product, "123", "string")

    def test_none_input(self):
        self.assertRaises(TypeError, largest_continuous_product, None, None)

    def test_float_input(self):
        self.assertRaises(TypeError, largest_continuous_product, "123", 3.1415)

    def test_bool_input(self):
        self.assertRaises(TypeError, largest_continuous_product, "123", True)

    def test_negative_input(self):
        self.assertRaises(ValueError, largest_continuous_product, "123", -10)

    def test_non_int_input(self):
        self.assertRaises(ValueError, largest_continuous_product, "123abc456", 4)

    def test_inconvenient_zero(self):
        self.assertEqual(largest_continuous_product("1230456", 4), 0)

    def test_around_zero(self):
        self.assertEqual(largest_continuous_product("1230456", 3), 120)

    def test_adjacent_is_length(self):
        self.assertEqual(largest_continuous_product("12312321", 8), 72)

    def test_adjacent_greater_than_length(self):
        self.assertEqual(largest_continuous_product("12312321", 13), 72)

    def test_regular(self):
        self.assertEqual(largest_continuous_product("1243376879865", 4), 4032)


if __name__ == '__main__':
    unittest.main()
