from abc import ABCMeta, abstractmethod

from src.reports.adapters.base import BaseReportAdapter
from src.reports.builders.base import BaseReportBuilder
from src.reports.filters.base import BaseReportFilter
from src.services.dealer.base import BaseWebService


class _BaseRepository(metaclass=ABCMeta):
    _service: BaseWebService
    _builder: BaseReportBuilder
    _filter: BaseReportFilter
    _adapter: BaseReportAdapter

    def __init__(
            self, service: BaseWebService,
            builder: BaseReportBuilder,
            reports_filter: BaseReportFilter,
            adapter: BaseReportAdapter):
        self._service = service
        self._builder = builder
        self._filter = reports_filter
        self._adapter = adapter


class BaseReadOnlyRepository(_BaseRepository, metaclass=ABCMeta):
    @abstractmethod
    async def get_all(self):
        pass


class BaseRepository(BaseReadOnlyRepository, metaclass=ABCMeta):
    @abstractmethod
    async def save(self, *args, **kwargs):
        pass
