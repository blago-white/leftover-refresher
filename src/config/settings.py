class SupplierWebSettings:
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
