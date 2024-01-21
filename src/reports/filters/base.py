from abc import ABCMeta, abstractmethod

from ..transfer.report import Report


class BaseReportFilter(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, report: Report) -> Report:
        pass
