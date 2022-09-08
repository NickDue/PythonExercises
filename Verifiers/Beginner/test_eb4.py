import unittest
from Exercises.Beginner.CatchException.CatchDivideByZeroException import *


class TestClass(unittest.TestCase):
    def test_case(self):
        with self.assertRaises(ZeroDivisionError):
            CatchDivisionByZero()


if __name__ == '__main__':
    unittest.main()
