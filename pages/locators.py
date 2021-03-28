from selenium.webdriver.common.by import By


class LoginPageLocators():
    URL = 'http://18.213.119.207/salesorder/pages/login.aspx'
    ACC_NUM = (By.CSS_SELECTOR, "input#ID_ACCOUNTNUMBER")
    LOGIN_ID = (By.CSS_SELECTOR, "#ID_USERNAME")
    PSWRD = (By.CSS_SELECTOR, "input#ID_PASSWORD")
    REMEMBER_ME = (By.CSS_SELECTOR, "#ID_REMEMBERME")
    LOGIN_BTN = (By.CSS_SELECTOR, "#ID_LOGIN")
    INVALID_LOGIN_TX = (By.CSS_SELECTOR, "#ID_LOGIN_ERROR > div > label > span")


class MainPageLocators:
    SHORTCUTS = (By.CSS_SELECTOR, "#shortcuts")
    EXPLORITARY_MENU = (By.CSS_SELECTOR, "#tree")
    WORK_SPACE = (By.CSS_SELECTOR, "#work")
    COLLAPSE_BTN = (By.CSS_SELECTOR, "#tabPanel > nav > div.tree-controls.group > a.collapse.group")
    SALES = (By.XPATH, '//*[@id="Sales"]/h2/a')
    SO = (By.CSS_SELECTOR, "#\30\.AllSalesOrders span")
