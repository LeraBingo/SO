from pages.apl_page import Apls
from pages.login_page import LoginPage


class TestApls:

    def test_list_all_apls(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        apl = Apls(browser, link)
        apl.list_all_apls()