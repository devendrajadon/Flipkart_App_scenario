from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.Locators import PageLocators

class SearchPage(BasePage):
    def __init__(self, driver):
        """Initializes the SearchPage with the provided WebDriver.
            Maximizes the browser window and navigates to the base URL. """
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(TestData.BaseUrl)

    def do_search(self):
        """
             Performs a search for a iPhone on the flipcart.
             - Clicks on the search box element.
             - Inputs the search text (iPhone model) into the search box.
             - Verifies if the search results are displayed.
             - Retrieves and prints the price of the specified iPhone model.

             :raises AssertionError: If the iPhone price element is not enabled or visible.
             """
        self.do_click(PageLocators.searchBox)
        self.do_send_keys(PageLocators.searchBox, TestData.search_iphone)
        self.press_enter_key(PageLocators.searchBox)
        flag = self.is_enabled(PageLocators.iphone_price)
        assert flag == True
        iphone_cost = self.get_element_text(PageLocators.iphone_price)
        print(f"Price of {TestData.iphone_model}: {iphone_cost}")





