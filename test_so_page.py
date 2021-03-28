import pytest
from pages.sales_orders_page import SalesOrder as SO
from pages.login_page import LoginPage

class TestSO:

    def test_go_to_so_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link, timeout=30)
        so.go_to_so()


