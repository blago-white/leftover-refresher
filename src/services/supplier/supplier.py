import logging
import os
import pathlib
import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from src.config.settings import SupplierSettings
from .base import BaseSupplierReportSeleniumParser
from .exceptions import ReportDownloadingTimeoutException

from ._utils import add_downloading_driver_options, add_default_options_args


class SupplierXLSReportService(BaseSupplierReportSeleniumParser):
    _REPORT_PATH: str = str(pathlib.Path(
        __name__
    ).absolute().parent / "src/static")

    _DEFAULT_OPTS_CLASS = ChromeOptions
    _DEFAULT_WEBDRIVER = Chrome
    _DEFAULT_REPORT_NAME = "ostatki_1630.xlsx"

    _DOWNLOAD_TIMEOUT = 10*60
    _DOWNLOAD_STATUS_CHECk_DELAY = 0.5

    def get(self) -> bytes:
        self._login()

        self._load_report()

        return self._return_as_bytes()

    def _login(self):
        self._driver.get(SupplierSettings.LOGIN_URL)

        WebDriverWait(self._driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.ID, SupplierSettings.USERNAME_FIELD_NAME)
            )
        )

        self._driver.find_element(
            By.ID, SupplierSettings.USERNAME_FIELD_NAME
        ).send_keys(self._CREDENTALS.username)

        self._driver.find_element(
            By.ID, SupplierSettings.PASSWORD_FIELD_NAME
        ).send_keys(self._CREDENTALS.password, Keys.ENTER)

    def _load_report(self):
        self._driver.get(SupplierSettings.LEFTOVER_URL)

        WebDriverWait(self._driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.ID, "peczat")
            )
        )

        self._driver.find_element(By.ID, "peczat").click()

    def _return_as_bytes(self) -> bytes:
        for _ in range(self._DOWNLOAD_TIMEOUT):
            time.sleep(self._DOWNLOAD_STATUS_CHECk_DELAY)

            try:
                with open(self._report_full_path, "rb") as f:
                    result = f.read()
                    break
            except:
                pass
        else:
            raise ReportDownloadingTimeoutException(
                "Supplier report does not loaded"
            )

        self._drop_used_report_file()

        return result

    def _drop_used_report_file(self):
        os.remove(self._report_full_path)

    @property
    def _default_driver(self):
        opts = self._DEFAULT_OPTS_CLASS()

        add_downloading_driver_options(
            options=opts,
            download_path=self._REPORT_PATH
        )

        add_default_options_args(options=opts)

        return self._DEFAULT_WEBDRIVER(options=opts)

    @property
    def _report_full_path(self):
        return self._REPORT_PATH + f"\\{self._DEFAULT_REPORT_NAME}"
