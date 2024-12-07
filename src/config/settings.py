import logging
import pathlib

from src.reports.transfer.filters.fields import leftover
from src.reports.transfer.filters.leftover import LeftoverValueFilter


_CONFIG_DIR = pathlib.Path(__file__).resolve().parent


class SupplierSettings:
    USERNAME_FIELD_NAME = "txtUserName"
    PASSWORD_FIELD_NAME = "txtPassword"

    LEFTOVER_URL = "https://lk.promet.ru/Sklad/SkladV"
    LOGIN_URL = "https://lk.promet.ru/default/"

    ARTICLE_CODE_COL_NUMBER = 1
    ARTICLE_LEFTOVER_COL_NUMBER = 3

    ARTICLE_LEFTOVER_VALUE_TYPE = int
    ARTICLE_CODE_VALUE_TYPE = str

    ARTICLE_LEFTOVER_FILTER = LeftoverValueFilter(
        filters=[leftover.LeftoverMinValueFieldFilter(0),
                 leftover.LeftoverMaxValueFieldFilter(10)]
    )


class DealerSettings:
    STOCKS_API_URL = "https://api-seller.ozon.ru/v3/product/info/stocks"
    STOCKS_UPDATE_API_URL = "https://api-seller.ozon.ru/v2/products/stocks"
    STOCKS_FOR_OWNER_API_URL = "https://api-seller.ozon.ru/v3/product/info/stocks"
    STOCKS_FOR_OWNER_SKU_API_URL = "https://api-seller.ozon.ru/v2/product/info/list"

    STOCKS_INFO_DICT_KEY = "result"
    STOCKS_ITEMS_DICT_KEY = "items"
    STOCKS_PRESENT_KEY = "present"
    STOCKS_KEY = "stocks"

    CLIENT_ID_HEADER = "Client-Id"
    API_KEY_HEADER = "Api-Key"

    SKU_BODY_PARAM = "sku"
    STOCKS_PARAM = "stocks"
    OFFER_ID_PARAM = "offer_id"
    PRODUCT_ID_PARAM = "product_id"
    NEW_STOCK_PARAM = "stock"
    WAREHOUSE_PARAM = "warehouse_id"

    WAREHOUSE_ID = 1020001281723000

    ARTICLES_MAX_COUNT = 2

    TRACKED_ARTICLES_JSON_PATH = _CONFIG_DIR / "tracked.json"

    ARTICLES_LIMIT_PER_REQUEST = 1000


class ConfigSettings:
    CONFIG_FILE_PATH = _CONFIG_DIR / "config.ini"


class LoggingSettings:
    LOG_FILE_PATH = _CONFIG_DIR.parent / "debug.log"
    DEFAULT_LOGGING_MODE = logging.DEBUG
    LOG_FORMAT = "%(asctime)s / %(pathname)s / %(message)s"
