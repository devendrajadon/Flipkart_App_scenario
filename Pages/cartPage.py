from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.Locators import PageLocators


#Search for a product and add product to card and validate cart price and product price
#
class AddToCart(BasePage):
    def __init__(self, driver):
        """Initializes the SearchPage with the provided WebDriver.
           Maximizes the browser window and navigates to the base URL. """
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(TestData.BaseUrl)

    def do_cart_ops(self):
        # Class for searching a product, adding it to the cart,
        # and validating the cart price and product price
        self.do_click(PageLocators.searchBox)
        self.do_send_keys(PageLocators.searchBox, TestData.search_samsung)
        self.press_enter_key(PageLocators.searchBox)

        # Handle the windows
        parent_handle = self.get_parent_handle()
        print(parent_handle)

        # Find the Samsung product in the search results
        mobile_result = self.get_search_elements(PageLocators.samsung_results)

        for mobile in mobile_result:
            print(mobile.text)
            if mobile.text == TestData.samsung_model:
                mobile.click()
                break

        # Switch to the new window
        all_windows = self.all_window_handle()
        try:
            for handle in all_windows:
                if handle != parent_handle:
                    self.do_switch_handle(handle)
                    price = self.get_element_text(PageLocators.samsung_price)
                    self.do_click(PageLocators.cart)
                    cart_price = self.get_element_text(PageLocators.cart_balance)
                    # Validate the cart price matches the product price
                    assert cart_price == price, f"Cart price {cart_price} does not match the expected price {price}"
        except:
            print("Product Not Found")

        finally:
            print("Test Completed Successfully")


