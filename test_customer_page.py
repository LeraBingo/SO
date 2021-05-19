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
        time.sleep(3)
        cus.save_new_cus()

    def test_go_to_customers_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        cus = CU(browser, link)
        cus.list_all_customers()

