from pages.items_page import Items
from pages.login_page import LoginPage
import random



class TestItems:

    def test_create_stock_item_with_descr_up_uc(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = random.random()
        it.creating_stock_item_with_decr_up_uc(f'lera{code}','stock',100,10)
        it.save_item()

    def test_create_stock_item_with_descr_up_uc_cat_cls(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()
        code = random.random()
        it.creating_stock_item_with_decr_up_uc(f'lera{code}', 'stock', 100, 10)
        it.add_class_and_category_to_item('newww', 'new cl')
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