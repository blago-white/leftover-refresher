from abc import ABCMeta, abstractmethod


class BaseReportBuilder(metaclass=ABCMeta):
    @property
    @abstractmethod
    def report(self):
        pass
