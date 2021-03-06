from selenium.webdriver.common.by import By

class AplPageLocators:
    APL_APPLY_TO_DROPDOWN = (By.CSS_SELECTOR, "#applyTo")
    APL_DESCRIPTION = (By.CSS_SELECTOR, "#description")
    APL_CREATE_NEW = (By.CSS_SELECTOR, "#_header_text~ul>li>button")
    APL_CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#currency")
    APL_CUS_DISCOUNT_METHOD_DROPDOWN = (By.CSS_SELECTOR, "#priceDiscountMethod")
    APL_DELETE = (By.XPATH, "//a[text()[contains(.,'Delete')]]")
    APL_EXCLUDE_CHECKBOX = (By.CSS_SELECTOR, "#_exclusive")
    APL_GENERAL_COST_DISCOUNT = (By.CSS_SELECTOR, "#costDefaultDiscount")
    APL_GENERAL_PRICE_DISCOUNT = (By.CSS_SELECTOR, "#priceDefaultDiscount")
    APL_HEADER_TX = (By.CSS_SELECTOR, "#_header_text")
    APL_HEADER_TX_APL_NAME = (By.CSS_SELECTOR, "#_inst")
    APL_NAME = (By.CSS_SELECTOR, "#name")
    APL_COST_FORMULA = (By.CSS_SELECTOR, "#costDefaultQuantityFormula")
    APL_PRICE_FORMULA = (By.CSS_SELECTOR, "#priceDefaultQuantityFormula")
    APL_SAVE = (By.XPATH, "//a[text()[contains(.,'Save')]]")
    APL_SUP_DISCOUNT_METHOD_DROPDOWN = (By.CSS_SELECTOR, "#costDiscountMethod")
    APL_USE_AS_DEFAULT_CUS_CHECKBOX = (By.CSS_SELECTOR, "#_isDefaultForCustomers")
    APL_USE_AS_DEFAULT_SUP_CHECKBOX = (By.CSS_SELECTOR, "#_isDefaultForSuppliers")
    CONFIRM_DELETING_BTN = (By.CSS_SELECTOR, "div.jconfirm-buttons>button:nth-child(1)")
    NUM_OF_ROWS_IN_APL_TABLE =  (By.XPATH, "//table[@id='advancedPriceLists_table']/tbody/tr")
    LIST_ALL_APLS_TABLE = (By.CSS_SELECTOR, "#advancedPriceLists_table_header")
    MSG_ABOUT_APL_DELETED = (By.CSS_SELECTOR, "#message")
    SEARCH_BTN = (By.CSS_SELECTOR, "#quickSearch")
    SEARCH_BY_APL_NAME = (By.CSS_SELECTOR, "#quickSearchName")
    TABLE_APLS = (By.CSS_SELECTOR, "#advancedPriceLists_table tbody td:nth-child(3)")
    VIEW_ICON = (By.CSS_SELECTOR, "tbody > tr:nth-child(1) > td > a.search-icon")

class CustomerPageLocators:
    CUS_ACTIONS = (By.XPATH, "//a[text()[contains(.,'Actions')]]")
    CUS_ADVANCED_SEARCH_TAB = (By.CSS_SELECTOR, "#tab2 > a")
    CUS_BALANCE_FROM_TBL = (By.XPATH, "//table[@id='customers_table']/tbody/tr/td[6]")
    CUS_CHECKBOX_IN_TABLE = (By.XPATH, '//*[@id="ms_customers.0"]')
    CUS_CREATE_NEW = (By.CSS_SELECTOR, "#_header_text~ul>li:first-child>button")
    CUS_CURRENCY = (By.CSS_SELECTOR, "#currency")
    CUS_DELETE = (By.XPATH, "//a[text()[contains(.,'Delete')]]")
    CUS_DELETE_CUSTOMERS = (By.XPATH, "//a[text()[contains(.,'Delete Customers')]]")
    CUS_EDIT = (By.XPATH, "//a[text()[contains(.,'Edit')]]")
    CUS_EXPORT_ALERT = (By.XPATH, "//div[@class='jconfirm-buttons']/button")
    CUS_EXPORT_CHECKBOX = (By.CSS_SELECTOR, "#_export")
    CUS_HEADER_TX = (By.CSS_SELECTOR, "#_header_text")
    CUS_LIST_MEMOS = (By.CSS_SELECTOR, "h1#_header_text~ul li:nth-child(3) button")
    CUS_MEMO_ICON = (By.CSS_SELECTOR, "h1#_header_text~ul li:nth-child(4) button")
    CUS_NAME = (By.CSS_SELECTOR, "#partnerName")
    CUS_NAME_IN_SEARCH = (By.CSS_SELECTOR, "#sName")
    CUS_NAMES_FROM_TBL = (By.XPATH, "//table[@id='customers_table']/tbody/tr/td[4]")
    CUS_NEW_SO_OPTION = (By.XPATH, "//a[text()[contains(.,'New Sales Order')]]")
    CUS_PL = (By.CSS_SELECTOR, "#priceList")
    CUS_PROFILE_TAB = (By.XPATH, "//a[contains(text(),'Profile')]")
    CUS_REFS_FROM_TBL = (By.XPATH, "//table[@id='customers_table']/tbody/tr/td[5]")
    CUS_SAVE_BTN = (By.CSS_SELECTOR, "#save")
    CUS_SAVE_NEW_CUS_BTN = (By.CSS_SELECTOR, "#construct")
    CUS_SEARCH = (By.CSS_SELECTOR, "#_search")
    CUS_VIEW_ICON = (By.XPATH, '//*[@id="customers_table"]/tbody/tr[1]/td[2]/a[3]')



class ItemPageLocators:
    BOM_FIND_ITEM = (By.CSS_SELECTOR, "#ptr_itemPtr_li\.0 > a.dbc-find-ITEMS.list.find-btn")
    CONFIRM_DELETING_BTN = (By.CSS_SELECTOR, "div.jconfirm-buttons>button:nth-child(1)")
    DELETE_ITEM_BTN = (By.XPATH, "//a[text()[contains(.,'Delete')]]")
    EDIT_ITEM = (By.XPATH, "//a[text()[contains(.,'Edit')]]")
    HAS_SERIAL_NUMBER_CHECKBOX = (By.CSS_SELECTOR, "#_hasSerialNumber")
    HEADER_TX_EDIT_ITEM = (By.CSS_SELECTOR, "#_header_text")
    HEADER_TX_VIEW_ITEM = (By.CSS_SELECTOR, "#_inst")
    ITEMS_BOM_TAB = (By.XPATH, "//nav[@class='custom-tabs group']/ul/li/a[contains(text(),'BOM')]")
    ITEM_CATEGORY_1 = (By.CSS_SELECTOR, "#cat1")
    ITEM_CATEGORY_2 = (By.CSS_SELECTOR, "#cat2")
    ITEM_CLASS = (By.CSS_SELECTOR, "#type1")
    ITEMS_CLASSIFICATION_TAB = (By.CSS_SELECTOR, "#tab4 > a")
    ITEM_CODES_IN_THE_TBL = (By.XPATH, '//*[@id="itemList_table"]/tbody/tr/td[3]')
    ITEMS_ITEM_CODE = (By.CSS_SELECTOR, "#itemCode")
    ITEMS_ITEM_DESCRIPTION = (By.CSS_SELECTOR, "#description")
    ITEMS_ITEM_UC = (By.CSS_SELECTOR, "#costPrice")
    ITEMS_ITEM_UP = (By.CSS_SELECTOR, "#itemPrice")
    ITEMS_MULTIPACK_SECTION = (By.CSS_SELECTOR, "#Multi-packs")
    ITEMS_PURCHASING_COST_TAB = (By.XPATH, '//a[contains(text(),"Purchasing/Costs")]')
    ITEMS_STOCK_TAB = (By.CSS_SELECTOR, "//nav[@class='custom-tabs group']/ul/li/a[contains(text(),'Stock')]")
    ITEMS_UOM_SECTION = (By.CSS_SELECTOR, "#Units\ of\ measure\ relationships")
    MSG_ABOUT_ITEM_DELETED = (By.CSS_SELECTOR, "#message")
    MULTIPACK_BARCODE= (By.CSS_SELECTOR, "#barcode_uoms\.0")
    MULTIPACK_NAME = (By.CSS_SELECTOR, "#name_uoms\.0")
    MULTIPACK_UNITS = (By.CSS_SELECTOR, "#stockUnits_uoms\.0")
    NEW_ASSEMBLY_ITEM = (By.CSS_SELECTOR, "#assemblyItem")
    NEW_KIT_ITEM = (By.CSS_SELECTOR, "#kitItem")
    NEW_STOCK_ITEM = (By.CSS_SELECTOR, "#stockItem")
    NUM_OF_ROWS_IN_ITEM_TABLE = (By.XPATH, "//table[@id='itemList_table']/tbody/tr")
    SAVE_BTN_FOR_EDITED_ITEM = (By.CSS_SELECTOR, "#save")
    SEARCH_BY_ITEM_CODE = (By.CSS_SELECTOR, "#byItemCode")
    SEARCH_BTN = (By.CSS_SELECTOR, "#searchByItemCode")
    TABLE_ITEM_CODES = (By.CSS_SELECTOR, "tbody td:nth-child(3)")
    UOM_SALES_UNITS = (By.CSS_SELECTOR, "#ratioSales")
    UOM_STOCK_UNITS = (By.CSS_SELECTOR, "#umStock")
    UOM_PURCHASE_UNITS = (By.CSS_SELECTOR, "#ratioPurchasing")
    VIEW_ICON = (By.CSS_SELECTOR, "tbody > tr:nth-child(1) > td > a.search-icon")



class LoginPageLocators:
    ACC_NUM = (By.CSS_SELECTOR, "input#ID_ACCOUNTNUMBER")
    INVALID_LOGIN_TX = (By.CSS_SELECTOR, "#ID_LOGIN_ERROR > div > label > span")
    LOGIN_BTN = (By.CSS_SELECTOR, "#ID_LOGIN")
    LOGIN_ID = (By.CSS_SELECTOR, "#ID_USERNAME")
    PSWRD = (By.CSS_SELECTOR, "input#ID_PASSWORD")
    REMEMBER_ME = (By.CSS_SELECTOR, "#ID_REMEMBERME")
    URL = 'http://18.213.119.207/salesorder/pages/login.aspx'


class MainPageLocators:
    ADD_ITEM_IN_ITEM_SELECTOR = (By.XPATH, "//tr[1]/td/img[@alt='add']")
    ADD_TRNX_OR_ITEM = (By.XPATH, '//ul[2]/li[1]/button')
    APL_DROPDOWN = (By.CSS_SELECTOR, "#priceList")
    APLS = (By.XPATH, "//li/a/span[contains(text(), 'Advanced Price Lists')]")
    APPLY_IN_ITEM_SEARCH = (By.XPATH, "//*[@id='apply']")
    BACK_BTN = (By.XPATH, "//div[@class='title-bar group']/ul/li/button/img")
    COLLAPSE_BTN = (By.CSS_SELECTOR, "#tabPanel > nav > div.tree-controls.group > a.collapse.group")
    CONFIRM_DELETING_BTN = (By.CSS_SELECTOR, "div.jconfirm-buttons>button:nth-child(1)")
    CREATE_NEW = (By.XPATH, "(//a[contains(text(),'Create New')])")
    CUSTOMERS =  (By.XPATH, "//li/a/span[starts-with(text(), 'Customers')]")

    EDIT_TRNX = (By.XPATH, "//a/img[contains(@alt, 'edit')]")
    EXPLORITARY_MENU = (By.CSS_SELECTOR, "#tree")
    EXPORT_HERE_LINK = (By.CSS_SELECTOR, "#message > a")

    FIND_ITEM = (By.CSS_SELECTOR, "#ptr_itemPtr_li\.0 > a.dbc-find-ITEMS.list.find-btn")

    HEADER_TX = (By.CSS_SELECTOR, "#_header_text")

    ITEMS = (By.XPATH, "//li/a/span[contains(text(), 'Items')]")

    LIST_ALL = (By.CSS_SELECTOR,
                '#Form1 > div > div > div.title-action-bar-container > div.action-bar.group > nav > ul > li:nth-child(5) > a')
    LIST_ALL_ITEMS = (By.XPATH, "//*[contains(a, 'List all Items')]")
    LIST_ALL_ITEMS_TABLE = (By.XPATH, '//*[@id="panel1"]/section[3]')

    MAGNIFYING_GLASS_VIEW_SO = (
        By.CSS_SELECTOR, "#invoices_table > tbody > tr > td.idb-table-3-actions-td.nw > a.search-icon")
    MEMO_DETAIL_TAB = (By.CSS_SELECTOR, "#tab2 > a")
    MEMO_EMAIL_REMAINDER_CHECKBOX = (By.CSS_SELECTOR, "#_emailReminderYN")
    MEMO_SUBJECT = (By.CSS_SELECTOR, "#subject")
    MEMO_TBL_SUBJECT_COLUMN = (By.XPATH, '//*[@id="memos_table"]/tbody/tr/td[2]')
    MSG_ABOUT_SUCCESSFUL_DELETION = (By.CSS_SELECTOR, "#message")
    NEXT_BTN = (By.XPATH, '//a[contains(text(),"Next")]')
    ORDER_REF_NUMBER = (By.CSS_SELECTOR, '#objectUID')

    PLEVEL_VALUE = (By.XPATH, '//*[@id="priceLevel"]/p')
    PLUS_FOR_ITEMS =(By.XPATH, "//li/a/span[contains(text(), 'Items')]/button")
    PL_VALUE = (By.XPATH, '//*[@id="priceList"]/p')
    PRODUCTS_SERVICES = (By.XPATH, '//*[@id="Inventory"]/h2')

    SALES = (By.XPATH, "//section[@id='Sales']/h2/a[contains(text(), 'Sales')]")
    SAVE = (By.CSS_SELECTOR, "#construct")
    SAVE_AFTER_EDIT = (By.CSS_SELECTOR, "#save")
    SEARCH_BTN_IN_ITEM_SELECTOR = (By.CSS_SELECTOR, "section#ItemsView input.search-button")
    SEARCH_BY_REF = (By.CSS_SELECTOR, "#byRefNum")
    SEARCH_ITEM_IN_ITEM_SELECTOR = (By.CSS_SELECTOR, "#itemSelectorSearchField")
    SEARCH_TRNXS = (By.CSS_SELECTOR, "#searchByReference")
    SHORTCUTS = (By.CSS_SELECTOR, "#shortcuts")
    SO = (By.XPATH, "//li/a/span[contains(text(), 'Sales Orders')]")

    TAX_VALUE = (By.XPATH, '//*[@id="taxCode"]/p')

    WORK_SPACE = (By.CSS_SELECTOR, "#work")
