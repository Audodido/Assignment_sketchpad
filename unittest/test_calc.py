import calc
import unittest


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 20), 30)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 20), -10)

    def test_mult(self):
        self.assertEqual(calc.mult(10, 20), 200)

    def test_div(self):
        self.assertEqual(calc.div(10, 20), .5)


if __name__ == "__main__":

    unittest.main()
