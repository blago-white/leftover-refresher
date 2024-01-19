from abc import ABCMeta, abstractmethod

from src.reports.utils import difference
from ._dataclasses import ReportBuildersPair
from .base import Controller


class BaseArticlesReportsController(Controller, metaclass=ABCMeta):
    _reports_pair: ReportBuildersPair

    @abstractmethod
    def _refresh_reports(self):
        pass


class ArticlesReportsController(BaseArticlesReportsController):
    def __init__(self, difference_calculator: difference.ReportsDifferenceCalculator):
        self._reports_pair = None

    async def refresh(self):
        await self._refresh_reports()
        self._get_difference()
        await self._commit_difference()

    async def _refresh_reports(self):
        #  TODO: Updates _reports_pair
        pass

    async def _commit_difference(self):
        #  TODO: Call save method from the slave
        pass

    def _get_difference(self):
        #  TODO: Returns diff between two reports
        pass
