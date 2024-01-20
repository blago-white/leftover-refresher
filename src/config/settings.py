import logging
import pathlib


class SupplierSettings:
    VIEWSTATE_FIELD_NAME = "__VIEWSTATE"
    GENERATOR_FIELD_NAME = "__VIEWSTATEGENERATOR"
    EVENTVALIDATION_FIELD_NAME = "__EVENTVALIDATION"

    USERNAME_FIELD_NAME = "txtUserName"
    PASSWORD_FIELD_NAME = "txtPassword"

    SKLAD_ID_FIELD_NAME = "ddlsklad"
    REPORT_DATE_FIELD_NAME = "data_akt"
    PL_FIELD_NAME = "pl"
    REPORT_FORMAT_FIELD_NAME = "peczat"

    SKLAD_ID = 6
    PL = 1630
    REPORT_FORMAT = "XLS"

    LEFTOVER_URL = "https://lk.promet.ru/Sklad/Sklad"
    LOGIN_URL = "https://lk.promet.ru/default/"

    DATE_FORMAT = "%d.%m.%Y"

    DUMMY_FORM_FIELDS = (
        "__EVENTARGUMENT",
        "__EVENTTARGET",
        "__LASTFOCUS",
    )

    LOGIN_FORM_FIELDS = (
        VIEWSTATE_FIELD_NAME,
        GENERATOR_FIELD_NAME,
        EVENTVALIDATION_FIELD_NAME,
        USERNAME_FIELD_NAME,
        PASSWORD_FIELD_NAME,
        *DUMMY_FORM_FIELDS,
        "btnLogin",
        "tb2"
    )

    LEFTOVERS_FORM_FIELDS = (
        VIEWSTATE_FIELD_NAME,
        GENERATOR_FIELD_NAME,
        EVENTVALIDATION_FIELD_NAME,
        *DUMMY_FORM_FIELDS,
        "__VIEWSTATEENCRYPTED",
        "Status",
        "pl",
        "ddlsklad",
        "data_akt",
        "peczat",
    )

    TRACKED_ARTICLES = (
        "S24499375509"
    )

    ARTICLE_CODE_COL_NUMBER = 1
    ARTICLE_LEFTOVER_COL_NUMBER = 3

    ARTICLE_LEFTOVER_VALUE_TYPE = int
    ARTICLE_CODE_VALUE_TYPE = str


class DealerSettings:
    STOCKS_API_URL = "https://api-seller.ozon.ru/v1/product/info/stocks-by-warehouse/fbs"
    STOCKS_UPDATE_API_URL = "https://api-seller.ozon.ru/v2/products/stocks"

    STOCKS_INFO_DICT_KEY = "result"
    STOCKS_PRESENT_KEY = "present"

    CLIENT_ID_HEADER = "Client-Id"
    API_KEY_HEADER = "Api-Key"

    TRACKED_SKUS = [
        1389650398,
    ]

    TRACKED_PRODUCTS_IDS = [
        837206055,
    ]

    SKU_BODY_PARAM = "sku"
    STOCKS_PARAM = "stocks"
    OFFER_ID_PARAM = "offer_id"
    PRODUCT_ID_PARAM = "product_id"
    NEW_STOCK_PARAM = "stock"
    WAREHOUSE_PARAM = "warehouse_id"

    WAREHOUSE_ID = 1020001281723000


class ConfigSettings:
    CONFIG_FILE_PATH = pathlib.Path(__file__).resolve().parent / "config.ini"


class LoggingSettings:
    LOG_FILE_PATH = pathlib.Path(__file__).resolve().parent.parent / "debug.log"
    DEFAULT_LOGGING_MODE = logging.DEBUG
    LOG_FORMAT = "%(asctime)s / %(pathname)s / %(message)s"
