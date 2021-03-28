from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators as MPL


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_subsection(self, section, subsection):
        self.browser.find_element(*MPL.COLLAPSE_BTN).click()
        self.browser.find_element(section).click()
        self.browser.find_element(subsection).click()




    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

# gets a link

    def open(self):
        self.browser.get(self.url)


    def valid_login(self):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')

