import unittest
from Exercises.Beginner.AddTwoIntegers.AddTwoIntegers import *


class TestClass(unittest.TestCase):
    def test_case(self):
        number1 = 10
        number2 = 2
        expected = number1 + number2
        actual = AddTwoIntegers(number1, number2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
