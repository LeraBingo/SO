import pytest
from pages.login_page import LoginPage



class TestLogin:



    def test_valid_login(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'UserPes777', 'UserPes')


    invalid_acc = [r'  SOA424824', r'SOA424824   ', 'SOA4248 2 4']
    invalid_login = [r'  letmein', r'letmein   ', 'l et me in']
    invalid_password = [r'  letmein', r'letmein   ', 'l et me in']

    @pytest.mark.negative
    @pytest.mark.xfail
    @pytest.mark.parametrize('inv_acc', invalid_acc)
    def test_invalid_account(self, browser, inv_acc):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login(inv_acc, 'letmein', 'letmein')

    @pytest.mark.negative
    @pytest.mark.xfail
    @pytest.mark.parametrize('inv_login', invalid_login)
    def test_invalid_login(self, browser, inv_login):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', inv_login, 'letmein')

    @pytest.mark.negative
    @pytest.mark.xfail
    @pytest.mark.parametrize('inv_pass', invalid_password)
    def test_invalid_login(self, browser, inv_pass):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', inv_pass)







