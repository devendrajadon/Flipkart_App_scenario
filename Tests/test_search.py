from Pages.searchPage import SearchPage
from Tests.test_base import BaseTest


# Test class for verifying search functionality
class Test_search(BaseTest):
    # Test method to validate iPhone price
    def test_iphone_price(self):
        # Initialize the SearchPage object with the driver
        self.SearchPage = SearchPage(self.driver)

        # Perform the search operation
        self.SearchPage.do_search()
