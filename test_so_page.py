from pages.sales_orders_page import SalesOrder as SO
from pages.login_page import LoginPage
from pages.items_page import Items as IT
from pages.apl_page import Apls as APL
import random
import time


class TestSO:


    def test_go_to_so_list(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()

    def test_search_by_ref_view(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view()

    def test_create_so(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.create_so('0001', 'cats')

#TODO: will add several similar tests. each will test a part of apl. this one changes any up to 10. Needs assertions. Not committed
    # creates so with new item(s) and apl. The apl has only general price discount. Asserts item values.

    def test_create_so_with_new_items_and_apl_gen_disc(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')

        num_of_items = 1

        #for now uses existing item. uncomment the below for the test to create new item

        """it = IT(browser, link)
        it.list_all_items()
        
        item_codes = []
        item_code = f'lera{str(random.random())[:5]}'
        it.creating_stock_item_with_decr_up_uc(item_code, 'stock', 77, 10)
        item_codes.append(item_code)
        it.save_item()
        for item in range(num_of_items-1):
            browser.switch_to_default_content()
            item_code = f'lera{str(random.random())[:5]}'
            item_codes.append(item_code)
            it.add_stock_item_with_plus(item_code, 'stock', 100, 10)
            it.save_item()"""

        apl_name = 'lera0.8673'
        apl_values = [apl_name, '10%', 'USD', 'no', 'Use Unit Price', 'no', '10.00', 'skip']
        """browser.switch_to_default_content()
        apl = APL(browser, link)
        apl.list_all_apls()
        apl_name = 'lera' + str(random.random())[:6]
        apl_values =[apl_name, '10%', 'USD', 'no', 'Use Unit Price', 'no', '10.00', 'skip']
        apl.create_new_apl_apply_to_customer(*apl_values)"""

        browser.switch_to_default_content()
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_items_without_saving(num_of_items, 'lera0.607' ) #*item_codes

        time.sleep(5)
        items_values_before_apl = so.store_items_values(num_of_items)
        so.apply_pl(apl_name)
        items_values_after_apl = so.store_items_values(num_of_items)
        for item in range(len(items_values_before_apl)):
            assert items_values_before_apl[item]['code'] == items_values_after_apl[item]['code'], f'code before = {items_values_before_apl[item]["code"]} and after = {items_values_after_apl[item]["code"] }'
            assert items_values_before_apl[item]['descr'] == items_values_after_apl[item]['descr'], f'descr before = {items_values_before_apl[item]["descr"]} and after = {items_values_after_apl[item]["descr"]}'
            assert items_values_before_apl[item]['site'] == items_values_after_apl[item]['site'], f'site before = {items_values_before_apl[item]["site"]} and after = {items_values_after_apl[item]["site"]}'

            #TODO: must add checks and calculations. not committed
            if apl_values[4] == 'Use Unit Price':

                discount = float(apl_values[6])/100
                up_discounted_calculated = float(items_values_before_apl[item]['up'])*(1-discount)
                assert float(items_values_after_apl[item]['up']) == up_discounted_calculated, f'calculated up = {up_discounted_calculated}  and actual = {items_values_after_apl[item]["up"]}'
                assert items_values_before_apl[item]['qty'] == items_values_after_apl[item]['qty'], f'qty before = {items_values_before_apl[item]["qty"]} and after = {items_values_after_apl[item]["qty"]}'
                assert items_values_before_apl[item]['discount'] == items_values_after_apl[item]['discount'], f'discount before = {items_values_before_apl[item]["discount"]} and after = {items_values_after_apl[item]["discount"]}'
                assert items_values_before_apl[item]['total_discount'] == items_values_after_apl[item]['total_discount'], f'total_discount before = {items_values_before_apl[item]["total_discount"]} and after = {items_values_after_apl[item]["total_discount"]}'
                total_calculated = up_discounted_calculated*float(items_values_before_apl[item]['qty'])
                assert total_calculated  ==float( items_values_after_apl[item]['total']), f'total before = {total_calculated } and after = {float(items_values_after_apl[item]["total"])}'
        so.save_so()

    def test_create_so_with_several_existing_items_by_ref(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_items_found_by_ref(3, '0001', '0002', '0003')

    def test_create_so_with_several_new_items_by_ref(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        it = IT(browser, link)
        it.list_all_items()
        num_of_items = 2
        item_codes = []
        item_code = f'lera{str(random.random())[:5]}'
        it.creating_stock_item_with_decr_up_uc(item_code, 'stock', 100, 10)
        item_codes.append(item_code)
        it.save_item()
        for item in range(num_of_items-1):
            browser.switch_to_default_content()
            item_code = f'lera{str(random.random())[:5]}'
            item_codes.append(item_code)
            it.add_stock_item_with_plus(item_code, 'stock', 100, 10)
            it.save_item()
        browser.switch_to_default_content()
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_items_found_by_ref(2, *item_codes)

    def test_create_so_with_several_random_items(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.create_so_with_several_random_items(3)

    def test_edit_so(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view('SO10951')
        so.edit_so()


    def test_compare_items_values_before_and_after_edit(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view('SO10951')
        so.remember_order_item_values(3)

    def test_compare_order_values_before_and_after_edit(self, browser):
        link = 'http://18.213.119.207/salesorder/pages/login.aspx'
        page = LoginPage(browser, link)
        page.open()
        page.login('SOA424824', 'letmein', 'letmein')
        so = SO(browser, link)
        so.list_all_so()
        so.search_so_by_ref_and_view('SO10951')
        so.remember_order_values()

