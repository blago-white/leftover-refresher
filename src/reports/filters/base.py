from abc import ABCMeta, abstractmethod

from ..transfer.report import Report


class BaseReportFilter(metaclass=ABCMeta):
    @property
    @abstractmethod
    def result(self) -> Report:
        pass
