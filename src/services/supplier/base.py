from abc import abstractmethod, ABCMeta

from selenium.webdriver import Chrome

from src.config.config import SupplierCredentals


class BaseSeleniumParser(metaclass=ABCMeta):
    def __init__(self, driver: Chrome):
        self._driver = driver


class BaseSupplierReportSeleniumParser(BaseSeleniumParser, metaclass=ABCMeta):
    _REPORT_PATH: str
    _CREDENTALS: SupplierCredentals

    def __init__(self, credentals: SupplierCredentals,
                 driver: Chrome = None,
                 report_path: str = None):
        super().__init__(driver=driver or self._default_driver)

        self._CREDENTALS = credentals
        self._REPORT_PATH = report_path or self._REPORT_PATH

    @property
    @abstractmethod
    def _default_driver(self):
        pass

    @property
    @abstractmethod
    def _report_full_path(self):
        pass
