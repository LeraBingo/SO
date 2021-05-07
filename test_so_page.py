from pages.sales_orders_page import SalesOrder as SO
from pages.login_page import LoginPage
from pages.items_page import Items as IT
from pages.apl_page import Apls as APL
import random


class TestSO:


    def test_go_to_so_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()

    def test_search_by_ref_view(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view()

    def test_create_so(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.create_so('0001', 'cats')



    def test_create_so_with_new_items_and_apl(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = IT(browser, link)
        it.list_all_items()
        num_of_items = 1
        item_codes = []
        item_code = f'lera{str(random.random())[:5]}'
        it.creating_stock_item_with_decr_up_uc(item_code, 'stock', 77, 10)
        item_codes.append(item_code)
        it.save_item()
        for item in range(num_of_items-1):
            browser.switch_to_default_content()
            item_code = f'lera{str(random.random())[:5]}'
            item_codes.append(item_code)
            it.add_stock_item_with_plus(item_code, 'stock', 100, 10)
            it.save_item()

        browser.switch_to_default_content()
        apl = APL(browser, link)
        apl.list_all_apls()
        apl_name = 'lera' + str(random.random())[:5]
        apl.create_new_apl_apply_to_customer(apl_name, 'changes up to 10', 'USD', 'no', 'Use Unit Price', 'no', '10.00', 'skip')

        browser.switch_to_default_content()
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_items_and_apl(num_of_items, apl_name, *item_codes)

    def test_create_so_with_several_existing_items_by_ref(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_items_found_by_ref(3, '0001', '0002', '0003')

    def test_create_so_with_several_new_items_by_ref(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = IT(browser, link)
        it.list_all_items()
        num_of_items = 2
        item_codes = []
        item_code = f'lera{str(random.random())[:5]}'
        it.creating_stock_item_with_decr_up_uc(item_code, 'stock', 100, 10)
        item_codes.append(item_code)
        it.save_item()
        for item in range(num_of_items-1):
            browser.switch_to_default_content()
            item_code = f'lera{str(random.random())[:5]}'
            item_codes.append(item_code)
            it.add_stock_item_with_plus(item_code, 'stock', 100, 10)
            it.save_item()
        browser.switch_to_default_content()
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_items_found_by_ref(2, *item_codes)

    def test_create_so_with_several_random_items(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_random_items(3)

    def test_edit_so(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view('SO10951')
        so.edit_so()


    def test_compare_items_values_before_and_after_edit(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view('SO10951')
        so.remember_order_item_values(3)

    def test_compare_order_values_before_and_after_edit(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view('SO10951')
        so.remember_order_values()

