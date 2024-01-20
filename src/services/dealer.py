import logging

from aiohttp.client import ClientSession

from src.config.config import DealerCredentals
from src.config.settings import DealerSettings
from src.reports.transfer.report import Report
from src.services.base import BaseWebService
from src.services.mixins.api import DealerApiCredentalsMixin, DealerApiMixin


class DeallerWebService(DealerApiCredentalsMixin, DealerApiMixin, BaseWebService):
    auth_credentals: DealerCredentals

    def __init__(self, auth_credentals: DealerCredentals, aoihttp_session: ClientSession):
        super().__init__(auth_credentals=auth_credentals, aoihttp_session=aoihttp_session)

        self._add_auth_headers()

    async def get(self) -> dict:
        logging.debug("Dealer Get Request")

        async with self._session.post(
            url=DealerSettings.STOCKS_API_URL,
            data=self._get_leftovers_info_json(),
        ) as response:
            return await response.json()

    async def post(self, report: Report) -> dict:
        logging.debug("Dealer Save Request")

        async with self._session.post(
            url=DealerSettings.STOCKS_UPDATE_API_URL,
            data=self._get_update_leftovers_json(report=report)
        ) as response:
            return await response.json()
