import aiohttp
import functools

from src.config.config import SupplierAuthResources, SupplierCredentals

from ._dataclasses import SupplierClienState


def _asyncrequest():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            async with aiohttp.ClientSession() as session:
                return await func(*args, **kwargs | {"session": session})
        return wrapped
    return wrapper


class SupplierSessionWebServiceMixin:
    _auth_resources: SupplierAuthResources
    _client_state: SupplierClienState

    @property
    def session(self):
        return

    @_asyncrequest()
    async def auth(self, session: aiohttp.ClientSession):
        async with session.post(url=self._auth_resources.loginurl) as _:
            pass

    @_asyncrequest()
    async def get_state(self, session: aiohttp.ClientSession):
        async with session.get(self._auth_resources.loginurl) as response:
            return await response.text()
