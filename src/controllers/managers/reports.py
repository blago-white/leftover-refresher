import asyncio
import logging

from src.reports.transfer.report import ReportsPair
from .base import BaseRepositoriesManager
from ..dataclasses_ import RepositoriesPair


class RepositoriesPairManager(BaseRepositoriesManager):
    async def get_all(self) -> ReportsPair:
        slave_report, master_report = await asyncio.gather(
            self._repositories_pair.slave.get_all(),
            self._repositories_pair.master.get_all()
        )

        logging.debug(
            f"Reports are collected - {slave_report=}; {master_report=}")

        return ReportsPair(
            slave_report=slave_report,
            master_report=master_report
        )
