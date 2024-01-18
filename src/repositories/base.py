from abc import ABCMeta, abstractmethod

from src.services.base import BaseWebService


class _BaseRepository(metaclass=ABCMeta):
    _service: BaseWebService

    def __init__(self, service: BaseWebService):
        self._service = service


class BaseReadOnlyRepository(_BaseRepository, metaclass=ABCMeta):
    @abstractmethod
    async def get_all(self):
        pass


class BaseRepository(BaseReadOnlyRepository, metaclass=ABCMeta):
    @abstractmethod
    async def save(self, *args, **kwargs):
        pass
