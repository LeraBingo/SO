from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators as MPL



class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

# gets a link

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()




