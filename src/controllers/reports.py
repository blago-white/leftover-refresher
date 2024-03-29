import logging
from abc import ABCMeta, abstractmethod

from src.reports.transfer.report import Report, ReportsPair
from .base import Controller
from .dataclasses_ import RepositoriesPair
from .managers.base import BaseRepositoriesManager
from .managers.reports import RepositoriesPairManager


class BaseArticlesController(Controller, metaclass=ABCMeta):
    _repositories_pair: RepositoriesPair

    @abstractmethod
    async def _refresh_reports(self):
        pass


class ArticlesLeftoversController(BaseArticlesController):
    _reports_pair: ReportsPair = ReportsPair(
        slave_report=Report(),
        master_report=Report()
    )

    def __init__(
            self, repositories: RepositoriesPair,
            repositories_manager_class: BaseRepositoriesManager = RepositoriesPairManager):
        self._repositories_pair = repositories
        self._repositories_manager: BaseRepositoriesManager = repositories_manager_class(
            self._repositories_pair
        )

        logging.debug("Controller initialized")

    async def synchronize(self) -> None:
        await self._refresh_reports()
        await self._synchronize()

        logging.debug("Leftovers refreshed")

    async def _refresh_reports(self) -> None:
        self._reports_pair = await self._repositories_manager.get_all()

    async def _synchronize(self) -> None:
        reports_diff = self._reports_pair.difference

        logging.debug(f"Reports Difference: {reports_diff}")

        if reports_diff:
            await self._repositories_pair.slave.save(reports_diff)
