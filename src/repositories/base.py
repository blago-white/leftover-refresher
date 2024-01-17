from abc import ABCMeta, abstractmethod

from src.services.base import BaseWebService


class BaseRepository(metaclass=ABCMeta):
    _service: BaseWebService

    def __init__(self, service: BaseWebService):
        self._service = service

    @abstractmethod
    async def get(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_all(self):
        pass

    @abstractmethod
    async def save(self, *args, **kwargs):
        pass
