from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .locators import AplPageLocators as APL
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



class Apls(BasePage):

    # creates apl with apply to = customer.
    # if a parameter must be skipped - write 'skip' (implemented for gen_price_disc, formula)
    # for checkboxes write 'yes' to enable them
    # dropdown values should be fully matched!
    # mind decimal places for numbers

    def create_new_apl_apply_to_customer(self, name, descr, currency, use_as_def, disc_method, exclude, gen_price_disc, formula):
        self.browser.find_element(*APL.APL_CREATE_NEW).click()
        self.browser.find_element(*APL.APL_NAME).send_keys(name)
        self.browser.find_element(*APL.APL_DESCRIPTION).send_keys(descr)
        Select(self.browser.find_element(*APL.APL_CURRENCY_DROPDOWN)).select_by_visible_text(currency)
        if use_as_def == 'yes':
            self.browser.find_element(*APL.APL_USE_AS_DEFAULT_CUS_CHECKBOX).click()
        Select(self.browser.find_element(*APL.APL_CUS_DISCOUNT_METHOD_DROPDOWN)).select_by_visible_text(disc_method)
        if exclude == 'yes':
            self.browser.find_element(*APL.APL_EXCLUDE_CHECKBOX).click()
        if gen_price_disc != 'skip':
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(Keys.DELETE)
            self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).send_keys(gen_price_disc)
        if formula != 'skip':
            self.browser.find_element(*APL.APL_PRICE_FORMULA).send_keys(formula)
        time.sleep(5)
        self.save_new_apl(name)

        name_after_saving = self.browser.find_element(*APL.APL_NAME).get_attribute('value')
        description_after_saving = self.browser.find_element(*APL.APL_DESCRIPTION).get_attribute('value')
        currency_after_saving = self.browser.find_element(*APL.APL_CURRENCY_DROPDOWN).get_attribute('value')
        is_selected_default_checkbox = self.browser.find_element(*APL.APL_USE_AS_DEFAULT_CUS_CHECKBOX).is_selected()
        disc_method_after_saving =  self.browser.find_element(*APL.APL_CUS_DISCOUNT_METHOD_DROPDOWN).get_attribute('value')
        is_selected_exclude_checkbox = self.browser.find_element(*APL.APL_EXCLUDE_CHECKBOX).is_selected()
        gen_disc_after_saving = self.browser.find_element(*APL.APL_GENERAL_PRICE_DISCOUNT).get_attribute('value')
        formula_after_saving = self.browser.find_element(*APL.APL_PRICE_FORMULA).get_attribute('value')

        assert name == name_after_saving, f'expected name = {name}, actual name = {name_after_saving}'
        assert descr == description_after_saving, f'expected descr = {descr}, actual descr = {description_after_saving}'
        assert currency_after_saving.startswith(currency), f'expected currency = {currency}, actual currency = {currency_after_saving}'
        if use_as_def == 'yes':
            assert is_selected_default_checkbox == True, f'Use as default checkbox = {is_selected_default_checkbox}, expected = true'
        elif use_as_def == 'no':
            assert is_selected_default_checkbox == False, f'Use as default checkbox = {is_selected_default_checkbox}, expected = false'
        assert disc_method_after_saving.endswith(disc_method), f'expected method = {disc_method}, actual method = {disc_method_after_saving}'

        if exclude == 'yes':
            assert is_selected_exclude_checkbox == True, f'Use as default checkbox = {is_selected_exclude_checkbox}, expected = true'
        elif exclude == 'no':
            assert is_selected_exclude_checkbox == False, f'Use as default checkbox = {is_selected_exclude_checkbox}, expected = false'

        if gen_price_disc == 'skip':
            assert gen_disc_after_saving == '0.00', f'General discount = {gen_disc_after_saving}, expected = 0.00'
        else:
            assert gen_disc_after_saving == gen_price_disc, f'General discount  = {gen_disc_after_saving}, expected = {gen_price_disc}'

        if formula == 'skip':
            assert formula_after_saving == '', f'Formula = {formula_after_saving}, expected = should be empty'
        else:
            assert formula_after_saving == formula, f'Formula  = {formula_after_saving}, expected = {formula}'

        # creates apl with apply to = supply.
        # if a parameter must be skipped - write 'skip' (implemented for gen_disc, formula)
        # for checkboxes write 'yes' to enable them
        # dropdown values should be fully matched!
        #TODO: add assertions

    def create_new_apl_apply_to_supplier(self, apply_to, name, descr, currency, use_as_def, disc_method, exclude, gen_disc, formula):
        self.browser.find_element(*APL.APL_CREATE_NEW).click()
        Select(self.browser.find_element(*APL.APL_APPLY_TO_DROPDOWN)).select_by_visible_text(apply_to)
        self.browser.find_element(*APL.APL_NAME).send_keys(name)
        self.browser.find_element(*APL.APL_DESCRIPTION).send_keys(descr)
        Select(self.browser.find_element(*APL.APL_CURRENCY_DROPDOWN)).select_by_visible_text(currency)
        if use_as_def == 'yes':
            self.browser.find_element(*APL.APL_USE_AS_DEFAULT_SUP_CHECKBOX).click()
        Select(self.browser.find_element(*APL.APL_SUP_DISCOUNT_METHOD_DROPDOWN)).select_by_visible_text(disc_method)
        if exclude == 'yes':
            self.browser.find_element(*APL.APL_EXCLUDE_CHECKBOX).click()
        if gen_disc != 'skip':
            self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).send_keys(Keys.DELETE)
            self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).send_keys(gen_disc)
        if formula != 'skip':
            self.browser.find_element(*APL.APL_COST_FORMULA).send_keys(formula)
        time.sleep(5)
        self.save_new_apl(name)


        name_after_saving = self.browser.find_element(*APL.APL_NAME).get_attribute('value')
        description_after_saving = self.browser.find_element(*APL.APL_DESCRIPTION).get_attribute('value')
        currency_after_saving = self.browser.find_element(*APL.APL_CURRENCY_DROPDOWN).get_attribute('value')
        is_selected_default_checkbox = self.browser.find_element(*APL.APL_USE_AS_DEFAULT_SUP_CHECKBOX).is_selected()
        disc_method_after_saving =  self.browser.find_element(*APL.APL_SUP_DISCOUNT_METHOD_DROPDOWN).get_attribute('value')
        is_selected_exclude_checkbox = self.browser.find_element(*APL.APL_EXCLUDE_CHECKBOX).is_selected()
        gen_disc_after_saving = self.browser.find_element(*APL.APL_GENERAL_COST_DISCOUNT).get_attribute('value')
        formula_after_saving = self.browser.find_element(*APL.APL_COST_FORMULA).get_attribute('value')

        assert name == name_after_saving, f'expected name = {name}, actual name = {name_after_saving}'
        assert descr == description_after_saving, f'expected descr = {descr}, actual descr = {description_after_saving}'
        assert currency_after_saving.startswith(currency), f'expected currency = {currency}, actual currency = {currency_after_saving}'
        if use_as_def == 'yes':
            assert is_selected_default_checkbox == True, f'Use as default checkbox = {is_selected_default_checkbox}, expected = true'
        elif use_as_def == 'no':
            assert is_selected_default_checkbox == False, f'Use as default checkbox = {is_selected_default_checkbox}, expected = false'
        assert disc_method_after_saving.endswith(disc_method), f'expected method = {disc_method}, actual method = {disc_method_after_saving}'

        if exclude == 'yes':
            assert is_selected_exclude_checkbox == True, f'Use as default checkbox = {is_selected_exclude_checkbox}, expected = true'
        elif exclude == 'no':
            assert is_selected_exclude_checkbox == False, f'Use as default checkbox = {is_selected_exclude_checkbox}, expected = false'

        if gen_disc == 'skip':
            assert gen_disc_after_saving == '0.00', f'General discount = {gen_disc_after_saving}, expected = 0.00'
        else:
            assert gen_disc_after_saving == gen_disc, f'General discount  = {gen_disc_after_saving}, expected = {gen_disc}'

        if formula == 'skip':
            assert formula_after_saving == '', f'Formula = {formula_after_saving}, expected = should be empty'
        else:
            assert formula_after_saving == formula, f'Formula  = {formula_after_saving}, expected = {formula}'


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

