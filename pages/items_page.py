from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .locators import ItemPageLocators as IPL
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Items(BasePage):

    # selects a category + class

    def add_class_and_category_to_item(self, cat1, cls):
        self.browser.find_element(*IPL.ITEMS_CLASSIFICATION_TAB).click()
        Select(self.browser.find_element(*IPL.ITEM_CATEGORY_1)).select_by_visible_text(cat1)
        Select(self.browser.find_element(*IPL.ITEM_CLASS)).select_by_visible_text(cls)

    # creates a stock item with descr, up, uc. !Without saving it!


    def creating_stock_item_with_decr_up_uc(self, item_code, descr, up, uc):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*IPL.NEW_STOCK_ITEM).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.ITEMS_ITEM_DESCRIPTION).send_keys(descr)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(up)
        self.browser.find_element(*IPL.ITEMS_PURCHASING_COST_TAB).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(uc)




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

    # saves item, checks if it`s been saved

    def save_item(self):
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), f'Item has not been created'



