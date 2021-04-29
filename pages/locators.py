from selenium.webdriver.common.by import By


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
    APPLY_IN_ITEM_SEARCH = (By.XPATH, "//*[@id='apply']")

    COLLAPSE_BTN = (By.CSS_SELECTOR, "#tabPanel > nav > div.tree-controls.group > a.collapse.group")
    CREATE_NEW = (By.XPATH, "(//a[contains(text(),'Create New')])")

    EDIT_TRNX = (By.XPATH, "//a/img[contains(@alt, 'edit')]")
    EXPLORITARY_MENU = (By.CSS_SELECTOR, "#tree")

    FIND_ITEM = (By.CSS_SELECTOR, "#ptr_itemPtr_li\.0 > a.dbc-find-ITEMS.list.find-btn")

    HEADER_TX = (By.CSS_SELECTOR, "#_header_text")

    ITEMS = (By.XPATH, "//li/a/span[contains(text(), 'Items')]")

    LIST_ALL = (By.CSS_SELECTOR,
                '#Form1 > div > div > div.title-action-bar-container > div.action-bar.group > nav > ul > li:nth-child(5) > a')
    LIST_ALL_ITEMS = (By.XPATH, "//*[contains(a, 'List all Items')]")
    LIST_ALL_ITEMS_TABLE = (By.XPATH, '//*[@id="panel1"]/section[3]')

    MAGNIFYING_GLASS_VIEW_SO = (
        By.CSS_SELECTOR, "#invoices_table > tbody > tr > td.idb-table-3-actions-td.nw > a.search-icon")

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
