from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""This class is parent of all pages class"""
"""This class contents all generic methods and utilities"""
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def press_enter_key(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_search_elements(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        elements = self.driver.find_elements(*by_locator)
        return elements

    def get_parent_handle(self):
        parent_window = self.driver.current_window_handle
        return parent_window

    def all_window_handle(self):
        all_window = self.driver.window_handles
        return all_window

    def do_switch_handle(self, handle):
        self.driver.switch_to.window(handle)







