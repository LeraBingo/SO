from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .locators import ItemPageLocators as IPL
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random
import re

class Items(BasePage):


    def add_assembly_with_plus(self, item_code, descr, up, uc):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        element_to_hover_over = self.browser.find_element(*MPL.ITEMS)
        hover = ActionChains(self.browser).move_to_element(element_to_hover_over)
        hover.perform()
        self.browser.find_element(*MPL.PLUS_FOR_ITEMS).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*IPL.NEW_ASSEMBLY_ITEM).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.ITEMS_ITEM_DESCRIPTION).send_keys(descr)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(up)
        self.browser.find_element(*IPL.ITEMS_BOM_TAB).click()
        self.add_several_items_to_bom_by_ref(2, '0001', '0002')
        print('\nItem code -', item_code)

    def add_stock_item_with_plus(self, item_code, descr, up, uc):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        element_to_hover_over = self.browser.find_element(*MPL.ITEMS)
        hover = ActionChains(self.browser).move_to_element(element_to_hover_over)
        hover.perform()
        self.browser.find_element(*MPL.PLUS_FOR_ITEMS).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
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
        print('\nItem code -', item_code)

    def add_kit_with_plus(self, item_code, descr, up):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        element_to_hover_over = self.browser.find_element(*MPL.ITEMS)
        hover = ActionChains(self.browser).move_to_element(element_to_hover_over)
        hover.perform()
        self.browser.find_element(*MPL.PLUS_FOR_ITEMS).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*IPL.NEW_KIT_ITEM).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.ITEMS_ITEM_DESCRIPTION).send_keys(descr)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(up)
        self.browser.find_element(*IPL.ITEMS_BOM_TAB).click()
        self.add_several_items_to_bom_by_ref(2, '0001', '0002')
        print('\nItem code -', item_code)



    def add_multipack_to_item(self, name, barcode, units):
        self.browser.find_element(*IPL.ITEMS_STOCK_TAB).click()
        self.browser.find_element(*IPL.ITEMS_MULTIPACK_SECTION).click()
        self.browser.find_element(*IPL.MULTIPACK_NAME).send_keys(name)
        self.browser.find_element(*IPL.MULTIPACK_BARCODE).send_keys(barcode)
        self.browser.find_element(*IPL.MULTIPACK_UNITS).send_keys(units)



    # selects a category + class

    def add_class_and_category_to_item(self, cat1, cls):
        self.browser.find_element(*IPL.ITEMS_CLASSIFICATION_TAB).click()
        Select(self.browser.find_element(*IPL.ITEM_CATEGORY_1)).select_by_visible_text(cat1)
        Select(self.browser.find_element(*IPL.ITEM_CLASS)).select_by_visible_text(cls)

    # adds number_of_items to bom

    def add_several_items_to_bom_by_ref(self, number_of_items, *items):
        self.browser.find_element(*IPL.BOM_FIND_ITEM).click()
        for i in range(number_of_items):
            self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).send_keys(items[i])
            time.sleep(3)  # for the table to be refreshed
            self.browser.find_element(*MPL.ADD_ITEM_IN_ITEM_SELECTOR).click()
            self.browser.find_element(*MPL.SEARCH_ITEM_IN_ITEM_SELECTOR).clear()
        time.sleep(5)
        self.browser.find_element(*MPL.APPLY_IN_ITEM_SEARCH).click()

    # adds uom

    def add_uom_to_item(self, units, sales_ration, purchase_ration):
        self.browser.find_element(*IPL.ITEMS_STOCK_TAB).click()
        self.browser.find_element(*IPL.ITEMS_UOM_SECTION).click()
        self.browser.find_element(*IPL.UOM_STOCK_UNITS).send_keys(units)
        self.browser.find_element(*IPL.UOM_SALES_UNITS).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.UOM_SALES_UNITS).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.UOM_SALES_UNITS).send_keys(sales_ration)
        self.browser.find_element(*IPL.UOM_PURCHASE_UNITS).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.UOM_PURCHASE_UNITS).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.UOM_PURCHASE_UNITS).send_keys(purchase_ration)

    def create_specified_number_of_items(self, num_of_items, item_type):
        for item in range(num_of_items):
            self.browser.switch_to_default_content()
            item_code = f'lera{str(random.random())[:5]}'
            if item_type == 'stock':
                self.add_stock_item_with_plus(item_code, 'stock', 100, 10)
            elif item_type == 'kit':
                self.add_kit_with_plus(item_code, 'kit', 100)
            elif item_type == 'assembly':
                self.add_assembly_with_plus(item_code, 'assembly', 100, 10)
            self.save_item()

    # creates an assembly item with descr, up, uc. !Without saving it!

    def creating_assembly_with_decr_up_uc(self, item_code, descr, up, uc):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*IPL.NEW_ASSEMBLY_ITEM).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.ITEMS_ITEM_DESCRIPTION).send_keys(descr)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(up)

        self.browser.find_element(*IPL.ITEMS_BOM_TAB).click()
        self.add_several_items_to_bom_by_ref(2, '0001', '0002')

        self.browser.find_element(*IPL.ITEMS_PURCHASING_COST_TAB).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(uc)
        print('\nItem code -', item_code)

    def creating_kit_with_decr_up_uc(self, item_code, descr, up):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*IPL.NEW_KIT_ITEM).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.ITEMS_ITEM_DESCRIPTION).send_keys(descr)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(up)
        self.browser.find_element(*IPL.ITEMS_BOM_TAB).click()
        self.add_several_items_to_bom_by_ref(2, '0001', '0002')
        print('\nItem code -', item_code)

    # creates a stock item with descr, up, uc. !Without saving it!

    def creating_stock_item_with_decr_up_uc(self, item_code, descr, up, uc):
        self.browser.find_element(*MPL.ADD_TRNX_OR_ITEM).click()
        self.browser.find_element(*IPL.NEW_STOCK_ITEM).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.ITEMS_ITEM_DESCRIPTION).send_keys(descr)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UP).send_keys(up)

        time.sleep(5)
        self.browser.find_element(*IPL.ITEMS_PURCHASING_COST_TAB).click()
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(Keys.CONTROL + "a")
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(Keys.DELETE)
        self.browser.find_element(*IPL.ITEMS_ITEM_UC).send_keys(uc)
        print('\nItem code -', item_code)

    def delete_item(self, item_code):
        self.view_item(item_code)
        self.browser.find_element(*IPL.DELETE_ITEM_BTN).click()
        self.browser.find_element(*IPL.CONFIRM_DELETING_BTN).click()
        msg_after_deleting_item = self.browser.find_element(*IPL.MSG_ABOUT_ITEM_DELETED).text
        assert msg_after_deleting_item == 'Delete operation completed', f'Wrong text has been received - {msg_after_deleting_item}'

    # this is the basic: edit->save changes. Changes should be implemented separately

    def edit_item(self):
        self.browser.find_element(*IPL.EDIT_ITEM).click()
        header_tx = self.browser.find_element(*IPL.HEADER_TX_EDIT_ITEM).text
        assert header_tx.startswith('Edit')
        # here we do some stuff
        self.browser.find_element(*IPL.SAVE_BTN_FOR_EDITED_ITEM).click()
        header_text = self.browser.find_element(*MPL.HEADER_TX).text
        assert header_text.startswith('View'), f'The changes have not been saved'

    # list all the items. !Note! sometimes it selects 'Stock' instead of 'Items'. Needs to be investigated

    def list_all_items(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.COLLAPSE_BTN).click()
        self.browser.find_element(*MPL.PRODUCTS_SERVICES).click()
        time.sleep(2)
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

    # compares item_code searched with the item codes in the table.
    # !Regex can be improved! only positive flow presented!

    def search_by_item_code(self, item_code):
        self.browser.find_element(*IPL.SEARCH_BY_ITEM_CODE).send_keys(item_code)
        self.browser.find_element(*IPL.SEARCH_BTN).click()
        codes =self.browser.find_elements(*IPL.TABLE_ITEM_CODES)
        item_code = re.escape(item_code)
        pattern = re.sub('\\\\\*', '.', item_code)
        for code in codes:
            code = code.text
            assert re.match(pattern, code), f'Code {code} is not equal to the searched item code {item_code}'

    # !does not work with wildcards

    def view_item(self, item_code = '0001'):
        self.list_all_items()
        self.search_by_item_code(item_code)
        self.browser.find_element(*IPL.VIEW_ICON).click()
        header_item_code = self.browser.find_element(*IPL.HEADER_TX_VIEW_ITEM).text
        assert item_code == header_item_code





