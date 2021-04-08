import pytest
from pages.sales_orders_page import SalesOrder as SO
from pages.login_page import LoginPage
from selenium.common.exceptions import UnexpectedAlertPresentException


# pytest -k test_go_to_so_list

class TestSO:


    def test_go_to_so_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()

    def test_search_by_ref_view(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()
        so.search_so_by_ref_and_view()

    def test_create_so(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()
        so.create_so('0001', 'cats')

    def test_create_so_with_several_items_by_ref(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()
        so.create_so_with_several_items_found_by_ref(3, '0001', '0002', '0003')

    def test_create_so_with_several_random_items(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()
        so.create_so_with_several_random_items(5)

    def test_edit_so(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()
        so.search_so_by_ref_and_view()
        so.edit_so()

    def test_compare_values_before_and_after_edit(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.go_to_all_so()
        so.search_so_by_ref_and_view()
        so.remember_order_values()

