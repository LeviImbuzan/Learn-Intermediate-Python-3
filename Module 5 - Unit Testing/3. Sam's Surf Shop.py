import unittest
import datetime
import surfshop


# Importing the module under test (assuming it's named surfshop)
import surfshop

class SurfShopTests(unittest.TestCase):

    def setUp(self):
        # Creating a new instance of ShoppingCart for each test
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        # Test adding a single surfboard to the cart
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        # Test adding multiple surfboards to the cart
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()  # Resetting the cart for each iteration

    @unittest.skip
    def test_add_too_many_surfboards(self):
        # Test adding too many surfboards to the cart (skipped for now)
        self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

    @unittest.expectedFailure
    def test_apply_locals_discount(self):
    #     # Test applying locals discount (currently expected to fail)
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)

    def test_add_invalid_checkout_date(self):
        # Test setting an invalid checkout date
        date = datetime.datetime.now()
        self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, date)


unittest.main()
