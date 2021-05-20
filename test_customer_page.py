from pages.customer_page import Customers as CU
from pages.login_page import LoginPage
import time

class TestCustomers:

    def test_create_cus(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()
        cus.create_cus('testC', 'USD')
        cus.save_new_cus()

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

