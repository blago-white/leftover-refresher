import bs4

from src.config.settings import SupplierSettings
from .base import BaseStateParser
from ..states import states


class ClientStateHtmlParser(BaseStateParser):
    _html: str

    def __init__(self, html: str):
        self._html = html

    @property
    def state(self) -> states.SupplierClienState:
        return states.SupplierClienState(
            viewstate=self._get_viewstate(),
            generator=self._get_generator(),
            eventvalidation=self._get_eventvalidation()
        )

    def _get_viewstate(self):
        return self._get_hidden_value(SupplierSettings.VIEWSTATE_FIELD_NAME)

    def _get_generator(self):
        return self._get_hidden_value(SupplierSettings.GENERATOR_FIELD_NAME)

    def _get_eventvalidation(self):
        return self._get_hidden_value(
            SupplierSettings.EVENTVALIDATION_FIELD_NAME)

    def _get_hidden_value(self, tag_id: str):
        return bs4.BeautifulSoup(
            self._html, "html.parser"
        ).find(attrs={"id": tag_id}).get("value")
