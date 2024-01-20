import logging
from abc import ABCMeta, abstractmethod

from src.reports.transfer.report import Report, ReportsPair
from .base import Controller
from .dataclasses_ import RepositoriesPair
from .managers.base import BaseRepositoriesManager


class BaseArticlesController(Controller, metaclass=ABCMeta):
    _repositories_pair: RepositoriesPair

    @abstractmethod
    async def _refresh_reports(self):
        pass


class ArticlesLeftoversController(BaseArticlesController):
    _reports_pair: ReportsPair = ReportsPair(slave_report=Report(), master_report=Report())

    def __init__(self, repositories: RepositoriesPair,
                 repositories_manager_class: BaseRepositoriesManager):
        self._repositories_pair = repositories
        self._repositories_manager: BaseRepositoriesManager = repositories_manager_class(self._repositories_pair)

    async def synchronize(self) -> None:
        await self._refresh_reports()
        await self._synchronize()

    async def _refresh_reports(self) -> None:
        self._reports_pair = await self._repositories_manager.get_all()

    async def _synchronize(self) -> None:
        if self._reports_pair.difference:
            await self._repositories_pair.slave.save(self._reports_pair.difference)
