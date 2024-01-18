from abc import ABCMeta, abstractmethod

from ..adapters.base import BaseReportAdapter
from ..filters.base import BaseReportFilter


class BaseReportBuilder(metaclass=ABCMeta):
    _data: bytes
    _adapter: BaseReportAdapter
    _filter: BaseReportFilter

    def __init__(self, data: bytes, filter_: BaseReportFilter, adapter: BaseReportAdapter):
        self._data = data
        self._adapter = adapter
        self._filter = filter_

    @property
    @abstractmethod
    def report(self):
        pass
