from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators as MPL
from selenium.webdriver.support.ui import Select
import time
from pages.items_page import Items as IT


class SalesOrder(BasePage):

    # adds an item (using item search). Now it adds one specified item

    def add_item(self, item):
        self.browser.find_element(*MPL.FIND_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys(item)
        self.browser.find_element(*MPL.ADD_ITEM_IN_ITEM_SELECTOR).click()
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()

    # adds a specified number of items, ref# should be indicated in the test-func

    def add_several_items_by_ref(self, number_of_items, *items):
        self.browser.find_element(*MPL.FIND_ITEM).click()
        for i in range(number_of_items):
            self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys(items[i])
            time.sleep(2)  # for the table to be refreshed
            self.browser.find_element(*MPL.ADD_ITEM_IN_ITEM_SELECTOR).click()
            self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).clear()
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()

    # adds a specified number of the 1st n items + wildcards. The number of it items can be specified in the test-function

    def add_several_random_items(self, number_of_items):
        self.browser.find_element(*MPL.FIND_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys('*')
        self.browser.find_element(*MPL.SEARCH_BTN_IN_ITEM_SELECTOR).click()
        for item in range(1, number_of_items):
            self.browser.find_element(By.XPATH, f"//tr[{item}]/td/img[@alt='add']").click()
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()

    # applies the entered PL

    def apply_pl(self, pl):
        Select(self.browser.find_element(*MPL.APL_DROPDOWN)).select_by_visible_text(pl)

    # creates a SO with 1 item and a PL applied, checks order has been created

    def create_so(self, item, pl):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('C10008')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        self.browser.find_element(*MPL.CREATE_NEW).click()
        self.add_item(item)
        self.apply_pl(pl)
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), "Order has not been created"

    # creates a so with specified number_of_items, items are added by ref# (using item search)
    # !Without saving it

    def create_so_with_several_items_without_saving(self, number_of_items, *items):

        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('C10008')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        self.browser.find_element(*MPL.CREATE_NEW).click()
        self.add_several_items_by_ref(number_of_items, *items)


    # creates a so with specified number_of_items, items are added by ref# (using item search)

    def create_so_with_several_items_found_by_ref(self, number_of_items, *items):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('C10008')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        self.browser.find_element(*MPL.CREATE_NEW).click()
        self.add_several_items_by_ref(number_of_items, *items)
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), "Order has not been created"
        order_ref = self.browser.find_element(*MPL.ORDER_REF_NUMBER).get_attribute('value')
        print('\nOrder ref - ', order_ref)

    # creates a SO with several items(their number can be specified), checks the order has been created

    def create_so_with_several_random_items(self, number_of_items):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys('C10008')
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        self.browser.find_element(*MPL.CREATE_NEW).click()
        self.add_several_random_items(number_of_items)
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), "Order has not been created"

    # this is the basic: edit->save changes. Changes should be implemented separately

    def edit_so(self):
        self.browser.find_element(*MPL.EDIT_TRNX).click()
        # here we do some stuff
        self.browser.find_element(*MPL.SAVE_AFTER_EDIT).click()

    # shows all SOs

    def list_all_so(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.SALES).click()
        time.sleep(2)
        self.browser.find_element(*MPL.SO).click()
        self.browser.find_element(*MPL.SALES).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.LIST_ALL).click()

    # saves item values to dictionary and compares them with the values after edit->save. The number of items can be specified in num_of_items

    def remember_order_item_values(self, num_of_items):
        items_values_before_edit =  self.store_items_values(num_of_items)
        self.edit_so()
        items_values_after_edit = self.store_items_values(num_of_items)
        assert items_values_before_edit == items_values_after_edit, f'before = {items_values_before_edit} and after = {items_values_after_edit}'


    # saves PL, tax and price level before changing and compares them with values after edit->save

    def remember_order_values(self):
        order_general_values_before_edit = {'pl': '', 'tax': '', 'plevel': ''}
        order_general_values_after_edit = {'pl': '', 'tax': '', 'plevel': ''}
        order_general_values_before_edit['pl'] = self.browser.find_element(*MPL.PL_VALUE).text
        order_general_values_before_edit['tax'] = self.browser.find_element(*MPL.TAX_VALUE).text
        order_general_values_before_edit['plevel'] = self.browser.find_element(*MPL.PLEVEL_VALUE).text
        self.edit_so()
        order_general_values_after_edit['pl'] = self.browser.find_element(*MPL.PL_VALUE).text
        order_general_values_after_edit['tax'] = self.browser.find_element(*MPL.TAX_VALUE).text
        order_general_values_after_edit['plevel'] = self.browser.find_element(*MPL.PLEVEL_VALUE).text
        assert order_general_values_before_edit == order_general_values_after_edit, f'Actual data = {order_general_values_after_edit}, expected - {order_general_values_before_edit} '

    # searches a so by ref# (indicated in send_keys for now) and opens in

    def search_so_by_ref_and_view(self, order_ref):
        self.browser.find_element(*MPL.SEARCH_BY_REF).send_keys(order_ref)
        self.browser.find_element(*MPL.SEARCH_TRNXS).click()
        assert self.is_element_present(*MPL.MAGNIFYING_GLASS_VIEW_SO), "No orders with the ref#"
        self.browser.find_element(*MPL.MAGNIFYING_GLASS_VIEW_SO).click()

    #saves item values

    def store_items_values(self, num_of_items):
        items_values = []

        for item in range(1,num_of_items+1):
            item_values = {'code': '', 'descr': '', 'site': '', 'qty_invcd': '0', 'allocated': '0',
                                       'in_shipping': '0', 'shipped': '0', 'up': '0', 'qty': '0', 'discount': '0',
                                       'total_discount': '0', 'amount': '0', 'tax': '', 'tax_rate': '0', 'total': '0'}

            item_values['code'] = self.browser.find_element(By.XPATH, f"//*[@id='li_table']/tbody/tr[{item}]/td[4]").text
            item_values['site'] = self.browser.find_element(By.XPATH, f"//table[@id='li_table']/tbody/tr[{item}]/td[12]/input").get_attribute( 'value')
            item_values['up'] = self.browser.find_element(By.XPATH, f"//table[@id='li_table']/tbody/tr[{item}]/td[22]/input").get_attribute( 'value')
            item_values['qty'] = self.browser.find_element(By.XPATH, f"//table[@id='li_table']/tbody/tr[{item}]/td[23]/input").get_attribute( 'value')
            item_values['discount'] = self.browser.find_element(By.XPATH,  f"//table[@id='li_table']/tbody/tr[{item}]/td[24]/input").get_attribute( 'value')
            item_values['total_discount'] = self.browser.find_element(By.XPATH,  f"//table[@id='li_table']/tbody/tr[{item}]/td[25]/input").get_attribute( 'value')
            item_values['amount'] = self.browser.find_element(By.XPATH,  f"//table[@id='li_table']/tbody/tr[{item}]/td[26]/input").get_attribute( 'value')
            item_values['total'] = self.browser.find_element(By.XPATH, f"//table[@id='li_table']/tbody/tr[{item}]/td[30]/input").get_attribute('value')
            items_values.append(item_values)
        return items_values

    # saves the so

    def save_so(self):
        self.browser.find_element(*MPL.SAVE).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), "Order has not been created"
        order_ref = self.browser.find_element(*MPL.ORDER_REF_NUMBER).get_attribute('value')
        print('\nOrder ref - ', order_ref)

