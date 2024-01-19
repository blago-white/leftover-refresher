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
        'S10399010140',
        'S10399020140',
        'S26199201001',
        'S26199201501',
        'S50102163000',
        'S26199201009',
        'S70299234615'
    )

    ARTICLE_CODE_COL_NUMBER = 1
    ARTICLE_LEFTOVER_COL_NUMBER = 3

    ARTICLE_LEFTOVER_VALUE_TYPE = int
    ARTICLE_CODE_VALUE_TYPE = str


class DealerSettings:
    STOCKS_API_URL = "https://api-seller.ozon.ru/v1/product/info/stocks-by-warehouse/fbs"
    STOCKS_INFO_DICT_KEY = "result"
    STOCKS_PRESENT_KEY = "present"

    CLIENT_ID_HEADER = "Client-Id"
    API_KEY_HEADER = "Api-Key"

    TRACKED_SKUS = [
        1389650398,
        1391279102
    ]
    SKU_BODY_PARAM = "sku"
