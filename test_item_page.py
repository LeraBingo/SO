from pages.items_page import Items
from pages.login_page import LoginPage


class TestItems:
    def test_go_to_item_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = Items(browser, link)
        it.list_all_items()