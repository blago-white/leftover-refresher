from ..transfer.report import Report

from abc import ABCMeta, abstractmethod


class BaseReportFilter(metaclass=ABCMeta):
    _result: Report

    @property
    @abstractmethod
    def result(self):
        return self._result
