import unittest
from Exercises.Beginner.Sum_a_ListOfNumbers.ListSum import *


class TestClass(unittest.TestCase):
    def test_case(self):
        numbers = [1, 2, 3, 5, 8, 13, 21]
        expected = 53
        actual = sum_a_list_of_intergers(numbers)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
