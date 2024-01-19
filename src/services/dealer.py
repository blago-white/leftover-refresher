import asyncio

import aiohttp.client
from aiohttp.client import ClientSession

from src.config.config import DealerCredentals
from src.config.settings import DealerSettings
from src.services.base import BaseWebService
from src.services.mixins.api import DealerApiCredentalsMixin, DealerApiMixin

from src.services.transfer import UpdateReport, ArticleLeftoversUpdateForm


class DeallerWebService(DealerApiCredentalsMixin, DealerApiMixin, BaseWebService):
    def __init__(self, auth_credentals: DealerCredentals, aoihttp_session: ClientSession):
        self._auth_credentals = auth_credentals

        super().__init__(aoihttp_session=aoihttp_session)

        self._add_auth_headers()

    async def get(self) -> dict:
        async with self._session.post(
            url=DealerSettings.STOCKS_API_URL,
            data=self._get_leftovers_info_json(),
        ) as response:
            return await response.json()

    async def post(self, update_report: UpdateReport) -> dict:
        async with self._session.post(
            url=DealerSettings.STOCKS_UPDATE_API_URL,
            data=self._get_update_leftovers_json(update_report=update_report)
        ) as response:
            return await response.json()
