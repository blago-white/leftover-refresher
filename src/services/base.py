from abc import ABCMeta, abstractmethod

from aiohttp.client import ClientSession


class BaseAuthWebService(metaclass=ABCMeta):
    _auth_credentals: object
    _session: ClientSession

    def __init__(
            self, auth_credentals: object, aoihttp_session: ClientSession):
        self._auth_credentals = auth_credentals
        self._session = aoihttp_session


class BaseReadOnlyWebService(BaseAuthWebService, metaclass=ABCMeta):
    @abstractmethod
    def get(self, *args, **kwargs) -> bytes:
        pass


class BaseWebService(BaseReadOnlyWebService, metaclass=ABCMeta):
    @abstractmethod
    async def post(self, *args, **kwargs) -> bytes:
        pass
