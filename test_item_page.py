from pages.items_page import Items
from pages.login_page import LoginPage
import random
import time



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

    def test_go_to_item_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()

    def test_search_by_item_code(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        it.search_by_item_code('lera0.7*')

    def test_view_found_by_code_item(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.view_item()
