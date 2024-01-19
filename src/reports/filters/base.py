from abc import ABCMeta, abstractmethod

from ..transfer.report import Report


class BaseReportFilter(metaclass=ABCMeta):
    _result: Report

    @property
    @abstractmethod
    def result(self):
        return self._result
