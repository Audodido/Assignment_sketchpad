import pizzaparlor as parlor
import unittest


class ClassTesting(unittest.TestCase):

    # def test_PizzaShopTicket(self):
    #     self.assertEqual(parlor.PizzaShop.ticket, 'pepperoni for connor - prepared by kev')

    def test_PizzaShop(self):
        self.assertEqual(parlor.PizzaShop('mushroom','connor').ticket(), 'mushroom for connor - prepared by kev')


if __name__ == '__main__':

    unittest.main()





