import unittest

from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(25, factorial(4))


if __name__ == '__main__':
    unittest.main()
