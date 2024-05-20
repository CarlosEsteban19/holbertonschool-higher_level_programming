import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-10, 20, -30, 40]), 40)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.2]), 3.2)
        self.assertEqual(max_integer([-1.5, -2.7, -3.2]), -1.5)

    def test_strings(self):
        self.assertEqual(max_integer(["one", "two", "three"]), "four")


if __name__ == '__main__':
    unittest.main()
