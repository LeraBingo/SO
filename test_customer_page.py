from pages.customer_page import Customers as CU
from pages.login_page import LoginPage
from pages.items_page import Items
from pages.sales_orders_page import SalesOrder as SO
from pages.locators import MainPageLocators as MPL
import time

class TestCustomers:

    def test_create_cus(self, browser):
        cus_name = 'testC'
        cus_currency ='USD'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.create_cus(cus_name, cus_currency)
        cus.save_new_cus()


    def test_create_so_from_cus(self,browser):
        cus_name = '3M COMPANY'
        num_of_items = 2
        items = ['0001', '0002']

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.search_cus_by_ref(cus_name)
        cus.view_cus()
        cus.create_so_from_cus()
        so= SO(browser, link)
        so.add_several_items_by_ref(num_of_items, *items)
        so.save_so()

# creates so from customer and checks wether default cus pl has been applied
    def test_create_so_from_cus_with_cus_pl(self, browser):
        cus_name = '3M COMPANY'
        pl_name = '5110'
        num_of_items = 2
        items = ['0001', '0002']

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.search_cus_by_ref(cus_name)
        cus.view_cus()
        cus.edit_cus()
        cus.add_cus_pl(pl_name)
        cus.save_changes()
        cus.create_so_from_cus()
        so = SO(browser, link)
        so.add_several_items_by_ref(num_of_items, *items)
        so.save_so()
        actual_pl = browser.find_element(*MPL.PL_VALUE).text
        assert pl_name == actual_pl, f'expected pl - {pl_name}, actual pl - {actual_pl}'

    def test_create_and_delete_cus(self, browser):
        cus_name = 'testC'
        cus_currency = 'USD'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.create_cus(cus_name, cus_currency)
        cus.save_new_cus()
        cus.delete_cus()


    def test_create_and_delete_cus_from_grid(self, browser):
        cus_name = 'testC'
        cus_currency = 'USD'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.create_cus(cus_name, cus_currency)
        cus.save_new_cus()
        browser.switch_to_default_content()
        cus.list_all_customers()
        cus.search_cus_by_ref(cus_name)
        cus.delete_cus_from_grid()


    def test_go_to_customers_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()

    def test_search_view_cus(self, browser):
        cus_name = '3M COMPANY'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.search_cus_by_ref(cus_name)
        cus.view_cus()

