from abc import ABCMeta, abstractmethod

from aiohttp.client import ClientSession


class BaseReadOnlyWebService(metaclass=ABCMeta):
    _session: ClientSession

    def __init__(self, aoihttp_session: ClientSession):
        self._session = aoihttp_session

    @abstractmethod
    def get(self, *args, **kwargs) -> bytes:
        pass


class BaseWebService(BaseReadOnlyWebService, metaclass=ABCMeta):
    @abstractmethod
    async def post(self, *args, **kwargs) -> bytes:
        pass

