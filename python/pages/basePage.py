import unittest
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

    def _element_present(self, locator):
        try:
            self.driver.find_element_by_css_selector(locator)
        except NoSuchElementException, e: return False
        return True

    def _wait_for(self, locator):
        WebDriverWait(self.driver, 5).until(lambda driver : self._element_present(locator))

    def _find(self, locator):
        return self.driver.find_element_by_css_selector(locator)

    def _type(self, locator, text):
        self._find(locator).send_keys(text)

    def _submit(self, locator):
        self._find(locator).submit()

    def _visit(self, url):
        self.driver.get(url)
