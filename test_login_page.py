import pytest
from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')


    invalid_acc = [r'  SOA424824', r'SOA424824   ', 'SOA4248 2 4']

    @pytest.mark.negative
    @pytest.mark.xfail
    @pytest.mark.parametrize('inv_acc', invalid_acc)
    def test_invalid_login(self, browser, inv_acc):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login(inv_acc, 'letmein', 'letmein')




