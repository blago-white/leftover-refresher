from abc import ABCMeta, abstractmethod

from src.services.base import BaseWebService
from src.reports.adapters.base import BaseReportAdapter
from src.reports.builders.base import BaseReportBuilder


class _BaseRepository(metaclass=ABCMeta):
    _service: BaseWebService
    _builder: BaseReportBuilder
    _adapter: BaseReportAdapter

    def __init__(self, service: BaseWebService,
                 builder: BaseReportBuilder,
                 adapter: BaseReportAdapter):
        self._service = service
        self._builder = builder
        self._adapter = adapter


class BaseReadOnlyRepository(_BaseRepository, metaclass=ABCMeta):
    @abstractmethod
    async def get_all(self):
        pass


class BaseRepository(BaseReadOnlyRepository, metaclass=ABCMeta):
    @abstractmethod
    async def save(self, *args, **kwargs):
        pass
