from .base_page import BasePage
from .locators import CustomerPageLocators as CPL
from .locators import MainPageLocators as MPL
import time
from selenium.webdriver.support.ui import Select

class Customers(BasePage):

    # creating a customer. !without saving
    def create_cus(self, name, currency):
        self.browser.find_element(*CPL.CUS_CREATE_NEW).click()
        self.browser.find_element(*CPL.CUS_NAME).send_keys(name)
        Select(self.browser.find_element(*CPL.CUS_CURRENCY)).select_by_visible_text(currency)



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

    def save_new_cus(self):
        self.browser.find_element(*CPL.CUS_SAVE_BTN).click()
        header_text = self.browser.find_element(*CPL.CUS_HEADER_TX).text
        assert header_text.startswith('View'), f'View Customer'

    def search_cus_by_ref(self, name):
        self.browser.find_element(*CPL.CUS_ADVANCED_SEARCH_TAB).click()
        self.browser.find_element(*CPL.CUS_NAME_IN_SEARCH).send_keys(name)
        self.browser.find_element(*CPL.CUS_SEARCH).click()
        names = self.browser.find_elements(*CPL.CUS_NAMES_FROM_TBL)
        for n in names:
            n = n.text
            assert n.startswith(name), f'Expected name = {name}, actual name = {n}'

    def view_cus(self):
        self.browser.find_element(*CPL.CUS_VIEW_ICON).click()
        header_text = self.browser.find_element(*CPL.CUS_HEADER_TX).text
        assert header_text.startswith('View'), f'View Customer'

