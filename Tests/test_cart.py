from Pages.cartPage import AddToCart
from Tests.test_base import BaseTest


# Test class for verifying cart operations
class Test_search(BaseTest):
    # Test method to add a Samsung product to the cart and validate cart operations
    def test_samsung_cart(self):
        # Initialize the AddToCart page object with the WebDriver instance
        self.AddToCart = AddToCart(self.driver)

        # Perform cart operations  searching for the product, adding it to the cart, and validating cart price
        self.AddToCart.do_cart_ops()
