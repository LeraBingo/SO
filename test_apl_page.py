from pages.apl_page import Apls
from pages.login_page import LoginPage
import random
from pages.locators import AplPageLocators as APLoc

class TestApls:

    def test_create_apl_for_cus(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()
        name = 'lera'+str(random.random())[:5]
        apl.create_new_apl_apply_to_customer(name, 'test', 'GBP', 'no', 'Use Unit Price', 'yes', '10.00', '[1-:10.00%]' )
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

# delets ALL apls found by search pattern

    def test_delete_all_apls_of_certain_name(self, browser):
        apl_name_search_pattern = 'lera*'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()
        apl.search_by_apl_name(apl_name_search_pattern)
        num_of_rows = len(browser.find_elements(*APLoc.NUM_OF_ROWS_IN_APL_TABLE))
        for row in range(num_of_rows):
            apl.view_apl(apl_name_search_pattern)
            apl.delete_apl()
            browser.switch_to_default_content()
            apl.list_all_apls()
            apl.search_by_apl_name(apl_name_search_pattern)

    def test_list_all_apls(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()

    def test_view_apl_found_by_name(self, browser):
        apl_name = '5110'

        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()
        apl.search_by_apl_name(apl_name)
        apl.view_apl(apl_name)