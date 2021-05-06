from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .locators import AplPageLocators as APL
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



class Apls(BasePage):

    # creates apl with apply to = customer. !without saving it
    # if a parameter must be skipped - write 'skip' (implemented for gen_price_disc, formula)
    # for checkboxes write 'yes' to enable them
    # dropdown values should be fully matched!

    def create_new_apl_apply_to_customer(self, name, descr, currency, use_as_def, disc_method, exclude, gen_price_disc, formula):
        self.browser.find_element(*APL.APL_CREATE_NEW).click()
        self.browser.find_element(*APL.APL_NAME).send_keys(name)
        self.browser.find_element(*APL.APL_DESCRIPTION).send_keys(descr)
        Select(self.browser.find_element(*APL.APL_CURRENCY_DROPDOWN)).select_by_visible_text(currency)
        if use_as_def == 'yes':
            self.browser.find_element(*APL.APL_USE_AS_DEFAULT_CUS_CHECKBOX).click()
        Select(self.browser.find_element(*APL.APL_CUS_DISCOUNT_METHOD_DROPDOWN)).select_by_visible_text(disc_method)
        if exclude == 'yes':
            self.browser.find_element(*APL.APL_USE_AS_DEFAULT_CUS_CHECKBOX).click()
        if gen_price_disc != 'skip':
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(Keys.DELETE)
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(gen_price_disc)
        if formula != 'skip':
            self.browser.find_element(*APL.APL_PRICE_FORMULA).send_keys(formula)
        time.sleep(5)

        # creates apl with apply to = supply. !without saving it
        # if a parameter must be skipped - write 'skip' (implemented for gen_disc, formula)
        # for checkboxes write 'yes' to enable them
        # dropdown values should be fully matched!
        #TODO: skips general cost discoont.needs to be fixed

    def create_new_apl_apply_to_supplier(self, apply_to, name, descr, currency, use_as_def, disc_method, exclude, gen_disc,
                                         formula):
        self.browser.find_element(*APL.APL_CREATE_NEW).click()
        Select(self.browser.find_element(*APL.APL_APPLY_TO_DROPDOWN)).select_by_visible_text(apply_to)
        self.browser.find_element(*APL.APL_NAME).send_keys(name)
        self.browser.find_element(*APL.APL_DESCRIPTION).send_keys(descr)
        Select(self.browser.find_element(*APL.APL_CURRENCY_DROPDOWN)).select_by_visible_text(currency)
        if use_as_def == 'yes':
            self.browser.find_element(*APL.APL_USE_AS_DEFAULT_CUS_CHECKBOX).click()
        Select(self.browser.find_element(*APL.APL_SUP_DISCOUNT_METHOD_DROPDOWN)).select_by_visible_text(disc_method)
        if exclude == 'yes':
            self.browser.find_element(*APL.APL_USE_AS_DEFAULT_SUP_CHECKBOX).click()
        if gen_disc != 'skip':
            self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).send_keys(Keys.DELETE)
            self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).send_keys(gen_disc)
        if formula != 'skip':
            self.browser.find_element(*APL.APL_COST_FORMULA).send_keys(formula)
        time.sleep(10)


    def delete_apl(self):
        self.browser.find_element(*APL.APL_DELETE).click()
        self.browser.find_element(*APL.CONFIRM_DELETING_BTN).click()
        msg_after_deleting_apl = self.browser.find_element(*APL.MSG_ABOUT_APL_DELETED).text
        assert msg_after_deleting_apl == 'Delete operation completed', f'Wrong text has been received - {msg_after_deleting_apl}'



    def list_all_apls(self):
        frame = self.browser.find_element_by_css_selector('#tree')
        self.browser.switch_to.frame(frame)
        self.browser.find_element(*MPL.COLLAPSE_BTN).click()
        self.browser.find_element(*MPL.PRODUCTS_SERVICES).click()
        time.sleep(2)
        self.browser.find_element(*MPL.APLS).click()
        self.browser.switch_to.default_content()
        frame = self.browser.find_element_by_css_selector('#workarea')
        self.browser.switch_to.frame(frame)
        assert self.is_element_present(*APL.LIST_ALL_APLS_TABLE), 'The apl table is not present'


    def save_new_apl(self, name):
        self.browser.find_element(*APL.APL_SAVE).click()
        header_tx = f'{self.browser.find_element(*APL.APL_HEADER_TX).text}'
        assert header_tx == f'View Advanced Price List {name}', f'The actual text header is - {header_tx}'

