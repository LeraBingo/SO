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
    SALES = (By.CSS_SELECTOR, '#Sales > h2 > a')
    SO = (By.XPATH, "//li[@id='0.AllSalesOrders']/a/span")
    LIST_ALL = (By.CSS_SELECTOR, '#Form1 > div > div > div.title-action-bar-container > div.action-bar.group > nav > ul > li:nth-child(5) > a')
    SEARCH_BY_REF = (By.CSS_SELECTOR, "#byRefNum")
    SEARCH_TRNXS = (By.CSS_SELECTOR, "#searchByReference")
    MAGNIFYING_GLASS_VIEW_SO = (By.CSS_SELECTOR, "#invoices_table > tbody > tr > td.idb-table-3-actions-td.nw > a.search-icon")
    ADD_TRNX = (By.XPATH, '//ul[2]/li[1]/button')
    CREATE_NEW = (By.XPATH, "(//a[contains(text(),'Create New')])")
    SAVE = (By.CSS_SELECTOR, "#construct")
