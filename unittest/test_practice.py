import practice
import unittest


class IsConnor(unittest.TestCase):

    def test_name_is_connor(self):
        self.assertTrue(practice.is_name_con("connor"), True)

    def test_name_caps_connor(self):
        self.assertEqual(practice.is_name_con("Connor"), True)


if __name__ == "__main__":

    unittest.main()


