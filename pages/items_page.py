from .base_page import BasePage
from .locators import MainPageLocators as MPL


class Items(BasePage):

    def list_all_items(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.PRODUCTS_SERVICES).click()
        self.browser.find_element(*MPL.ITEMS).click()
        self.browser.switch_to.default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.LIST_ALL_ITEMS).click()
        assert self.is_element_present(*MPL.LIST_ALL_ITEMS_TABLE), 'The item table is not present'



