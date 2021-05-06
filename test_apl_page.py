from pages.apl_page import Apls
from pages.login_page import LoginPage
import random


class TestApls:

    def test_create_apl_for_cus(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()
        name = 'lera'+str(random.random())[:5]
        apl.create_new_apl_apply_to_customer(name, 'test', 'GBP', 'no', 'Use Discount', 'yes', '10.00', '[1-:10.00%]' )
        apl.delete_apl()

    def test_create_apl_for_sup(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()
        name = 'lera' + str(random.random())[:5]
        apl.create_new_apl_apply_to_supplier('Supplier', name, 'test', 'GBP', 'no', 'Use Unit Cost', 'yes', 'skip', '[1-:10.0000]')
        apl.delete_apl()

    def test_list_all_apls(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()