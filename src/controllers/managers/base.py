from abc import ABCMeta, abstractmethod

from src.reports.transfer.report import ReportsPair
from ..dataclasses_ import RepositoriesPair


class BaseRepositoriesManager(metaclass=ABCMeta):
    _repositories_pair: RepositoriesPair

    @abstractmethod
    def __init__(self, repositories: RepositoriesPair, *args, **kwargs):
        pass

    @abstractmethod
    def get_all(self) -> ReportsPair:
        pass
