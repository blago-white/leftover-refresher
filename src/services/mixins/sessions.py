import http
import logging
import aiohttp

from src.config.config import SupplierCredentals
from src.config.settings import SupplierSettings
from ..parsers.state import ClientStateHtmlParser
from ..states.states import SupplierClienState
from ..utils.request.login import get_login_body


class SupplierStatesWebServiceMixin:
    _session: aiohttp.ClientSession
    __client_state: SupplierClienState = None

    async def _set_state(self, state_url: str) -> SupplierClienState:
        logging.debug("Supplier Session Get Request")

        async with self._session.get(state_url) as response:
            self.__client_state = ClientStateHtmlParser(html=await response.text()).state

        logging.debug("Supplier Session Get Request Completed")

    @property
    def _state(self) -> SupplierClienState | None:
        return self.__client_state


class SupplierAuthWebServiceMixin(SupplierStatesWebServiceMixin):
    _auth_credentals: SupplierCredentals = None
    __authenticated = False

    async def _authenticate(self):
        await self._set_state(state_url=SupplierSettings.LOGIN_URL)

        body = get_login_body(
            state=self._state,
            credentals=self._auth_credentals
        )

        logging.debug("Supplier Auth Request")

        async with self._session.post(url=SupplierSettings.LOGIN_URL, data=body) as response:
            if response.status == http.HTTPStatus.OK:
                self.__authenticated = True

        logging.debug("Supplier Auth Request Completed")

    @property
    def _authenticated(self) -> bool:
        return self.__authenticated
