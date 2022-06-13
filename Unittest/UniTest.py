import unittest

class TestExample(unittest.TestCase):
    def test_sum_numbers(self):
        num1 = 10
        num2 = 20

        res = num1 + num2
        self.assertEqual(res, 30)

    def test_rest_numbers(self):
        num1 = 10
        num2 = 20

        res = num1 - num2
        self.assertEqual(res, -10)

if __name__ == '__main__':
    unittest.main()