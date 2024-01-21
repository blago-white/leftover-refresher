import logging

from aiohttp import ClientSession

from src.config.config import SupplierCredentals
from src.config.settings import SupplierSettings
from .base import BaseReadOnlyWebService
from .mixins import sessions
from .utils.request import leftover


class SupplierWebService(sessions.SupplierAuthWebServiceMixin,
                         BaseReadOnlyWebService):
    auth_credentals: SupplierCredentals

    def __init__(
            self, auth_credentals: SupplierCredentals,
            aoihttp_session: ClientSession):
        super().__init__(auth_credentals=auth_credentals,
                         aoihttp_session=aoihttp_session)

    async def get(self) -> bytes:
        if not self._authenticated:
            await self._authenticate()
            logging.debug("Supplier Auth Request Completed")

        await self._set_state(state_url=SupplierSettings.LEFTOVER_URL)

        leftover_request_body = leftover.get_leftover_form_body(
            state=self._state)

        logging.debug("Supplier Get Request")

        async with self._session.post(url=SupplierSettings.LEFTOVER_URL,
                                      data=leftover_request_body) as response:
            return await response.content.read()
