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

# takes cus data from excel and from the table and compares it.
# !now it fails as there is difference in number of spaces of customers
    def test_export_cus_tbl(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        data_from_excel = cus.export_cus_tbl()
        browser.switch_to.window(browser.window_handles[0]) # to switch back to the window with customers
        frame = browser.find_element_by_css_selector('#workarea')
        browser.switch_to.frame(frame)
        browser.find_element(*MPL.BACK_BTN).click()
        time.sleep(2)
        browser.find_element(*MPL.LIST_ALL).click()
        time.sleep(2)
        data_from_tbl = cus.get_cus_values_from_tbl()
        assert data_from_excel == data_from_tbl, f'data from excel = {data_from_excel}, data from tbl = {data_from_tbl}'

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

    def test_search_view_cus_add_memo(self, browser):
        cus_name = '3M COMPANY'
        subject = 'new2_subj'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.search_cus_by_ref(cus_name)
        cus.view_cus()
        cus.create_memo_for_cus(subject)
