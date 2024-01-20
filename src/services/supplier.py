from aiohttp import ClientSession

from src.config.config import SupplierCredentals
from src.config.settings import SupplierSettings
from .base import BaseReadOnlyWebService
from .mixins import sessions
from .utils.request import leftover


class SupplierLeftoversWebService(sessions.SupplierAuthWebServiceMixin, BaseReadOnlyWebService):
    def __init__(self, auth_credentals: SupplierCredentals, aoihttp_session: ClientSession):
        self._auth_credentals = auth_credentals
        super().__init__(aoihttp_session=aoihttp_session)

    async def get(self) -> bytes:
        if not self._authenticated:
            await self._authenticate()

        await self._set_state(state_url=SupplierSettings.LEFTOVER_URL)

        leftover_request_body = leftover.get_leftover_form_body(state=self._state)

        async with self._session.post(url=SupplierSettings.LEFTOVER_URL, data=leftover_request_body) as response:
            return await response.content.read()
