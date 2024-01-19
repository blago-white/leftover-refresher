from abc import ABCMeta, abstractmethod

from ..adapters.base import BaseReportAdapter
from ..filters.base import BaseReportFilter
from ..transfer.report import Report


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
    def report(self) -> Report:
        pass

    def _get_filtered(self, report: Report) -> Report:
        if self._filter:
            return self._filter(report).result

        return report


class DefaultReportBuilder(BaseReportBuilder):
    @property
    def report(self) -> Report:
        report = self._adapter(self._data).data

        return self._get_filtered(report=report)
