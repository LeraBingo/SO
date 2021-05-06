from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .locators import AplPageLocators as APL
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



class Apls(BasePage):

    # creates apl with apply to = customer. !without saving it
    # if a parametar must be skipped - write 'skip' (implemented for gen_price_disc, formula)
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
        if formula != 'skip':
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(Keys.DELETE)
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(gen_price_disc)
        if formula != 'skip':
            self.browser.find_element(*APL.APL_PRICE_FORMULA).send_keys(formula)
        time.sleep(5)






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