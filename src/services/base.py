from abc import ABCMeta, abstractmethod


class BaseWebService(metaclass=ABCMeta):
    @abstractmethod
    async def get(self, *args, **kwargs) -> bytes:
        pass

    @abstractmethod
    async def post(self, *args, **kwargs) -> bytes:
        pass
