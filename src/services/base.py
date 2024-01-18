from abc import ABCMeta, abstractmethod


class BaseReadOnlyWebService(metaclass=ABCMeta):
    @abstractmethod
    def get(self, *args, **kwargs) -> bytes:
        pass


class BaseWebService(BaseReadOnlyWebService, metaclass=ABCMeta):
    @abstractmethod
    async def post(self, *args, **kwargs) -> bytes:
        pass

