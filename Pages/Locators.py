from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData

class PageLocators(BasePage):
    # Locator for the search box input field in flipkart
    searchBox = (By.CSS_SELECTOR, "input[placeholder='Search for Products, Brands and More']")

    # Locator for Samsung Galaxy S24 Ultra 5G search results
    samsung_results = (By.XPATH, "//div[@class='KzDlHZ' and contains(text(), 'SAMSUNG Galaxy S24 Ultra 5G (Titanium Gray, 256 GB)')]")

    # Locator for the price of the Samsung Galaxy S24 Ultra 5G
    samsung_price = (By.XPATH, "//div[@class='Nx9bqj CxhGGd']")

    # Locator for the shopping cart icon
    cart = (By.CLASS_NAME, "NwyjNT")

    # Locator for the balance in the shopping cart
    cart_balance = (By.CLASS_NAME, "_1Y9Lgu")

    # Locator for the price of the iPhone model specified in TestData.iphone_model
    iphone_price = (By.XPATH, "//*[contains(text()," + TestData.iphone_model + ")]/parent::div/parent::div/child::div[@class=\"col col-5-12 BfVC2z\"]/descendant::div[@class=\"Nx9bqj _4b5DiR\"]")
