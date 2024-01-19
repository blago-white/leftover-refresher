import http

import aiohttp

from src.config.config import SupplierAuthResources
from ..parsers.state import ClientStateHtmlParser
from ..states.states import SupplierClienState
from ..utils.request.login import get_login_body


class SupplierStatesWebServiceMixin:
    _session: aiohttp.ClientSession
    __client_state: SupplierClienState = None

    async def _set_state(self, state_url: str) -> SupplierClienState:
        async with self._session.get(state_url) as response:
            self.__client_state = ClientStateHtmlParser(html=await response.text()).state

    @property
    def _state(self) -> SupplierClienState | None:
        return self.__client_state


class SupplierAuthWebServiceMixin(SupplierStatesWebServiceMixin):
    _auth_resources: SupplierAuthResources = None
    __authenticated = False

    async def _authenticate(self):
        await self._set_state(state_url=self._auth_resources.loginurl)

        body = get_login_body(
            state=self._state,
            credentals=self._auth_resources.credentals
        )

        async with self._session.post(url=self._auth_resources.loginurl, data=body) as response:
            if response.status == http.HTTPStatus.OK:
                self.__authenticated = True

    @property
    def _authenticated(self) -> bool:
        return self.__authenticated
