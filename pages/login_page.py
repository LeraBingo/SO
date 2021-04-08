from .base_page import BasePage
from .locators import LoginPageLocators as LPL
from .locators import MainPageLocators as MPL


class LoginPage(BasePage):

    # log in with provided data

    def login(self, acc, lgn, psw):
        self.should_be_register_form()  # checks if this is really a register form
        self.browser.find_element(*LPL.ACC_NUM).send_keys(acc)
        self.browser.find_element(*LPL.LOGIN_ID).send_keys(lgn)
        self.browser.find_element(*LPL.PSWRD).send_keys(psw)
        self.browser.find_element(*LPL.LOGIN_BTN).click()
        self.should_be_main_page()

    # check error msg in case of invalid login

    def should_be_error_text(self):
        assert self.is_element_present(*LPL.INVALID_LOGIN_TX), "Failed login with negative data"

    # check if this is main page

    def should_be_main_page(self):
        assert self.is_element_present(*MPL.WORK_SPACE), "Cannot find work frame"
        assert self.is_element_present(*MPL.EXPLORITARY_MENU), "Cannot find tree frame"

    # check if this is register form

    def should_be_register_form(self):
        assert self.is_element_present(*LPL.ACC_NUM), "Account number is not presented"
        assert self.is_element_present(*LPL.LOGIN_ID), "Login is not presented"
        assert self.is_element_present(*LPL.PSWRD), "Password is not presented"
