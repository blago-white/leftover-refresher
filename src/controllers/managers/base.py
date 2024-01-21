from abc import ABCMeta, abstractmethod

from src.reports.transfer.report import ReportsPair
from ..dataclasses_ import RepositoriesPair


class BaseRepositoriesManager(metaclass=ABCMeta):
    _repositories_pair: RepositoriesPair

    def __init__(self, repositories: RepositoriesPair, *args, **kwargs):
        self._repositories_pair = repositories

    @abstractmethod
    def get_all(self) -> ReportsPair:
        pass
