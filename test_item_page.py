from selenium.common.exceptions import NoSuchElementException
from pages.items_page import Items
from pages.login_page import LoginPage
import random
import time
from pages.locators import ItemPageLocators as IPL
from pages.locators import MainPageLocators as MPL
from selenium.webdriver.common.by import By




class TestItems:

    def test_create_assembly_item_with_descr_up_uc(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = str(random.random())[:5]
        it.creating_assembly_with_decr_up_uc(f'lera{code}', 'assembly', 100, 10)
        it.save_item()

    def test_create_kit_with_descr_up_uc(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424774', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = str(random.random())[:5]
        it.creating_kit_with_decr_up_uc(f'lera{code}', 'kit', 100)
        it.save_item()

    def test_create_specified_num_of_items(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.create_specified_number_of_items(2, 'assembly')

    def test_create_stock_item_with_descr_up_uc(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = str(random.random())[:5]
        it.creating_stock_item_with_decr_up_uc(f'lera{code}','stock',100,10)
        it.save_item()

    def test_create_stock_item_with_descr_up_uc_cat_cls(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = str(random.random())[:6]
        it.creating_stock_item_with_decr_up_uc(f'lera{code}', 'stock', 100, 10)
        it.add_class_and_category_to_item('newww', 'new cl')
        it.save_item()

    def test_create_stock_item_with_descr_up_uc_multipack(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code =str(random.random())[:4]
        it.creating_stock_item_with_decr_up_uc(f'lera{code}', 'stock', 100, 10)
        it.add_multipack_to_item(f'MPlera{code}', f'MPlera{code}', 2)
        it.save_item()

    def test_create_stock_item_with_descr_up_uc_uom(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = random.random()
        it.creating_stock_item_with_decr_up_uc(f'lera{code}', 'stock', 100, 10)
        it.add_uom_to_item('lera_units', 5, 10)
        it.save_item()

# deletes all the items matching itcem_code_search_pattern.
# if an iten is used in a document, it will be skipped

    def test_delete_all_items_of_certain_code(self, browser):
        item_code_search_pattern = 'lera*'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.search_by_item_code(item_code_search_pattern)
        num_of_rows = len(browser.find_elements(*IPL.NUM_OF_ROWS_IN_ITEM_TABLE))
        swith_to_next_item = 1
        for row in range(num_of_rows):
            VIEW_ICON = (By.CSS_SELECTOR, f"tbody > tr:nth-child({swith_to_next_item}) > td > a.search-icon")
            browser.find_element(*VIEW_ICON).click()
            try:
                it.delete_item()
            except NoSuchElementException:
                swith_to_next_item+=1
            finally:
                browser.switch_to_default_content()
                it.list_all_items()
                it.search_by_item_code(item_code_search_pattern)

    def test_delete_item(self, browser):
        item_code = 'lera0.5000890478592263'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.search_by_item_code(item_code)
        it.view_item()
        it.delete_item()


    def test_edit_item(self, browser):
        item_code = 'lera0.73'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.search_by_item_code(item_code)
        it.view_item()
        it.edit_item()

    def test_go_to_item_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424806', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()

    def test_search_by_item_code(self, browser):
        item_code = 'lera0.73'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.search_by_item_code(item_code)


    def test_search_duplicate_items_with_space_at_the_end(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424806', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.check_space_at_the_end_of_item_code()


    def test_view_found_by_code_item(self, browser):
        item_code = 'lera0.73'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.search_by_item_code(item_code)
        it.view_item()
