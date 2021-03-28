from .base_page import BasePage
from .locators import MainPageLocators as MPL


class SalesOrder(BasePage):

    def go_to_so(self):
        section = self.browser.find_element(*MPL.SALES)
        subsection = self.browser.find_element(*MPL.SO)
        self.go_to_subsection(section, subsection)
