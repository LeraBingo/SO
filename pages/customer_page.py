from pandas.tests.io.excel.test_openpyxl import openpyxl

from .base_page import BasePage
from .locators import CustomerPageLocators as CPL
from .locators import MainPageLocators as MPL
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy

class Customers(BasePage):

    def add_cus_pl(self, pl):
        self.browser.find_element(*CPL.CUS_PROFILE_TAB).click()
        Select(self.browser.find_element(*CPL.CUS_PL)).select_by_visible_text(pl)
        return pl


    # creating a customer. !without saving
    def create_cus(self, name, currency):
        self.browser.find_element(*CPL.CUS_CREATE_NEW).click()
        self.browser.find_element(*CPL.CUS_NAME).send_keys(name)
        Select(self.browser.find_element(*CPL.CUS_CURRENCY)).select_by_visible_text(currency)

    # creates a memo and checks whether it`s been created
    def create_memo_for_cus(self, subject):
        self.browser.find_element(*CPL.CUS_MEMO_ICON).click()
        frame = self.browser.find_element_by_css_selector('#popupFrame')
        self.browser.switch_to.frame(frame)
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.MEMO_SUBJECT).send_keys(subject)
        self.browser.find_element(*MPL.MEMO_DETAIL_TAB).click()
        self.browser.find_element(*MPL.MEMO_EMAIL_REMAINDER_CHECKBOX).click()
        self.browser.find_element(*MPL.SAVE).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)

        # below assertion goes
        self.browser.find_element(*CPL.CUS_LIST_MEMOS).click()
        frame = self.browser.find_element_by_css_selector('#popupFrame')
        self.browser.switch_to.frame(frame)
        memo_names = []
        for memo_name in self.browser.find_elements(*MPL.MEMO_TBL_SUBJECT_COLUMN):
            memo_names += [memo_name.text]
        assert subject in memo_names, f'Memo has not been created'

    # Actions -> Create New SO
    def create_so_from_cus(self):
        self.browser.find_element(*CPL.CUS_ACTIONS).click()
        self.browser.find_element(*CPL.CUS_NEW_SO_OPTION).click()

    def delete_cus(self):
        self.browser.find_element(*CPL.CUS_ACTIONS).click()
        self.browser.find_element(*CPL.CUS_DELETE).click()
        self.browser.find_element(*MPL.CONFIRM_DELETING_BTN).click()
        message_about_deletion = self.browser.find_element(*MPL.MSG_ABOUT_SUCCESSFUL_DELETION).text
        assert message_about_deletion == 'Delete operation completed', f'Actual msg = {message_about_deletion}'

    def delete_cus_from_grid(self):
        self.browser.find_element(*CPL.CUS_CHECKBOX_IN_TABLE).click()
        self.browser.find_element(*CPL.CUS_DELETE_CUSTOMERS).click()
        self.browser.find_element(*MPL.CONFIRM_DELETING_BTN).click()
        message_about_deletion = self.browser.find_element(*MPL.MSG_ABOUT_SUCCESSFUL_DELETION).text
        assert message_about_deletion == 'Successfully deleted 1 Customer.', f'Actual msg = {message_about_deletion}'


    def edit_cus(self):
        self.browser.find_element(*CPL.CUS_EDIT).click()
        header_text = self.browser.find_element(*CPL.CUS_HEADER_TX).text
        assert header_text.startswith('Edit'), f'The item has not been edited'

    # exports customer tbl, saves the excel data to the list, returns it
    def export_cus_tbl(self):

        # method to get the downloaded file name
        def getDownLoadedFileName(waitTime):
            self.browser.execute_script("window.open()")
            # switch to new tab
            self.browser.switch_to.window(self.browser.window_handles[-1])
            # navigate to chrome downloads
            self.browser.get('chrome://downloads')
            # define the endTime
            endTime = time.time() + waitTime
            while True:
                try:
                    # get downloaded percentage
                    downloadPercentage = self.browser.execute_script(
                        "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('#progress').value")
                    # check if downloadPercentage is 100 (otherwise the script will keep waiting)
                    if downloadPercentage == 100:
                        # return the file name once the download is completed
                        return self.browser.execute_script(
                            "return document.querySelector('downloads-manager').shadowRoot.querySelector('#downloadsList downloads-item').shadowRoot.querySelector('div#content  #file-link').text")
                except:
                    pass
                time.sleep(1)
                if time.time() > endTime:
                    break

        self.browser.find_element(*CPL.CUS_EXPORT_CHECKBOX).click()
        self.browser.find_element(*CPL.CUS_EXPORT_ALERT).click()
        self.browser.find_element(*MPL.LIST_ALL).click()
        self.browser.find_element(*MPL.EXPORT_HERE_LINK).click()
        file_name = getDownLoadedFileName(waitTime=5)
        #path = r"C:\Users\User\Downloads\export (69).xlsx"
        path = f'C:\\Users\\User\\Downloads\\{file_name}'
        exl = pd.read_excel(path, engine='openpyxl')
        values_for_cus = exl.values.tolist()
        return values_for_cus

    # takes cus name, ref# balance and returns them in a list. Balance is formatted to float
    def get_cus_values_from_tbl(self):
        data_from_tbl = [[],[],[]]

        def add_datum_to_lists(data_from_tbl):
            names, refs, balances = [], [], []
            names += self.browser.find_elements(*CPL.CUS_NAMES_FROM_TBL)
            for name in names:
                data_from_tbl[0]+=[name.text]
            refs += self.browser.find_elements(*CPL.CUS_REFS_FROM_TBL)
            for ref in refs:
                data_from_tbl[1]+=[ref.text]
            balances += self.browser.find_elements(*CPL.CUS_BALANCE_FROM_TBL)
            for balance in balances:
                balance = balance.text
                data_from_tbl[2]+=[balance]
            if self.is_element_present(*MPL.NEXT_BTN):
                self.browser.find_element(*MPL.NEXT_BTN).click()
                add_datum_to_lists(data_from_tbl)

        add_datum_to_lists(data_from_tbl)
        data_from_tbl = numpy.transpose(data_from_tbl).tolist()
        for line in data_from_tbl:
            line[2] = float(line[2].replace(',','')) # format from str to float
        return data_from_tbl


    def list_all_customers(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.SALES).click()
        time.sleep(2)
        self.browser.find_element(*MPL.CUSTOMERS).click()
        self.browser.find_element(*MPL.SALES).click()
        self.browser.switch_to_default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.LIST_ALL).click()

    def save_changes(self):
        self.browser.find_element(*CPL.CUS_SAVE_BTN).click()
        header_text = self.browser.find_element(*CPL.CUS_HEADER_TX).text
        assert header_text.startswith('View'), f'View Customer'

    def save_new_cus(self):
        self.browser.find_element(*CPL.CUS_SAVE_NEW_CUS_BTN).click()
        header_text = self.browser.find_element(*CPL.CUS_HEADER_TX).text
        assert header_text.startswith('View'), f'View Customer'

    def search_cus_by_ref(self, name):
        self.browser.find_element(*CPL.CUS_ADVANCED_SEARCH_TAB).click()
        self.browser.find_element(*CPL.CUS_NAME_IN_SEARCH).send_keys(name)
        self.browser.find_element(*CPL.CUS_SEARCH).click()
        names = self.browser.find_elements(*CPL.CUS_NAMES_FROM_TBL)
        for n in names:
            n = n.text
            assert n.startswith(name), f'Expected name = {name}, actual name = {n}'

    def view_cus(self):
        self.browser.find_element(*CPL.CUS_VIEW_ICON).click()
        header_text = self.browser.find_element(*CPL.CUS_HEADER_TX).text
        assert header_text.startswith('View'), f'View Customer'

