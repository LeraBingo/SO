from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .locators import AplPageLocators as APL
import time


class Apls(BasePage):

    def list_all_apls(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.COLLAPSE_BTN).click()
        self.browser.find_element(*MPL.PRODUCTS_SERVICES).click()
        time.sleep(2)
        self.browser.find_element(*MPL.APLS).click()
        self.browser.switch_to.default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        assert self.is_element_present(*APL.LIST_ALL_APLS_TABLE), 'The apl table is not present'