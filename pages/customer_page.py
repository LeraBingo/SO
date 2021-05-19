from .base_page import BasePage
from .locators import CustomerPageLocators as CPL
from .locators import MainPageLocators as MPL
import time

class Customers(BasePage):


    def list_all_customers(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.SALES).click()
        time.sleep(2)
        self.browser.find_element(*MPL.CUSTOMERS).click()
        self.browser.find_element(*MPL.SALES).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.LIST_ALL).click()
