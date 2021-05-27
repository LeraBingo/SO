from .base_page import BasePage
from .locators import CustomerPageLocators as CPL
from .locators import MainPageLocators as MPL
import time
from selenium.webdriver.support.ui import Select

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

