from src.reports.transfer.report import ReportsPair

from .base import BaseRepositoriesManager
from ..dataclasses_ import RepositoriesPair


class ReportsPairManager(BaseRepositoriesManager):
    def __init__(self, repositories: RepositoriesPair):
        self._repositories_pair = repositories

    async def get_all(self) -> ReportsPair:
        return ReportsPair(
            slave_report=await self._repositories_pair.slave.get_all(),
            master_report=await self._repositories_pair.master.get_all()
        )
