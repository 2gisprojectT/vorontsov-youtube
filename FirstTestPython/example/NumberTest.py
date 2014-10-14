from unittest import TestCase
from example import Numbers
import unittest

class NumbersTest(TestCase):

    def test_init(self):
        num = Numbers(1,-2,6)
        self.assertEqual(1, num.a, 'A have wrong value')
        self.assertEqual(-2, num.b, 'B have wrong value')
        self.assertEqual(6, num.c, 'C have wrong value')

        self.assertEqual(5, num.sum(), 'Wrong Summary')
        self.assertEqual(-12, num.multiplication(), 'Wrong multiplication')
        self.assertEqual(12, num.abs_multiplication(), 'Wrong abs multiplication')

    def test_init1(self):
        num = Numbers(1,2,-5)
        self.assertEqual(1, num.a, 'a wrong')
        self.assertEqual(2, num.b, 'b wrong')
        self.assertEqual(0, num.c, 'c wrong')

if __name__ == '__main__':
    unittest.main()


