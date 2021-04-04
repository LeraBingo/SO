
from .base_page import BasePage
from .locators import MainPageLocators as MPL
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SalesOrder(BasePage):

    def go_to_all_so(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.SALES).click()
        self.browser.find_element(*MPL.SO).click()
        self.browser.find_element(*MPL.SALES).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.LIST_ALL).click()



    def search_so_by_ref_and_view(self):
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('SO10897')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        assert self.is_element_present(*MPL.MAGNIFYING_GLASS_VIEW_SO), "No orders with the ref#"
        self.browser.find_element(*MPL.MAGNIFYING_GLASS_VIEW_SO).click()


    def create_so(self):
        self.browser.find_element(*MPL.ADD_TRNX).click()
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('C10008')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        self.browser.find_element(*MPL.CREATE_NEW).click()
        self.add_item()
        self.apply_pl()
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), "Order has not been created"


    def add_item(self):
        self.browser.find_element(*MPL.FIND_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys('0001')
        self.browser.find_element(*MPL.ADD_ITEM_IN_ITEM_SELECTOR).click()
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()

    def apply_pl(self):
        Select(self.browser.find_element(*MPL.APL_DROPDOWN)).select_by_visible_text('cats')









