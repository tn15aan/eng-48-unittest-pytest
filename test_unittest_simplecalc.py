import unittest
from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.add(4, 4), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 2), 6)
        self.assertEqual(self.calc.subtract(8, 4), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(6, 2), 3)

