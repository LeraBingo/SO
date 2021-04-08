from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators as MPL
from selenium.webdriver.support.ui import Select

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

    def create_so_with_several_items(self, number_of_items):
        self.browser.find_element(*MPL.ADD_TRNX).click()
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('C10008')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        self.browser.find_element(*MPL.CREATE_NEW).click()
        self.add_several_random_items(number_of_items)
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), "Order has not been created"


    def add_item(self):
        self.browser.find_element(*MPL.FIND_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys('0001')
        self.browser.find_element(*MPL.ADD_ITEM_IN_ITEM_SELECTOR).click()
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()

    def add_several_random_items(self, number_of_items):
        self.browser.find_element(*MPL.FIND_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys('*')
        self.browser.find_element(*MPL.SEARCH_BTN_IN_ITEM_SELECTOR).click()
        for item in range(1, number_of_items):
            self.browser.find_element(By.XPATH, f"//tr[{item}]/td/img[@alt='add']").click()
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()




    def apply_pl(self):
        Select(self.browser.find_element(*MPL.APL_DROPDOWN)).select_by_visible_text('cats')

    def edit_so(self):
        self.browser.find_element(*MPL.EDIT_TRNX).click()
        #here we do some stuff
        self.browser.find_element(*MPL.SAVE_AFTER_EDIT).click()


    def remember_order_values(self):
        order_general_values_before_edit = {'pl':'', 'tax':'', 'plevel':''}
        order_general_values_after_edit = {'pl': '', 'tax': '', 'plevel': ''}
        order_general_values_before_edit['pl'] =  self.browser.find_element(*MPL.PL_VALUE).text
        order_general_values_before_edit['tax'] = self.browser.find_element(*MPL.TAX_VALUE).text
        order_general_values_before_edit['plevel']  = self.browser.find_element(*MPL.PLEVEL_VALUE).text
        self.edit_so()
        order_general_values_after_edit['pl'] = self.browser.find_element(*MPL.PL_VALUE).text
        order_general_values_after_edit['tax'] = self.browser.find_element(*MPL.TAX_VALUE).text
        order_general_values_after_edit['plevel'] = self.browser.find_element(*MPL.PLEVEL_VALUE).text
        assert order_general_values_before_edit == order_general_values_after_edit, f'Actual data = {order_general_values_after_edit}, expected - {order_general_values_before_edit} '








