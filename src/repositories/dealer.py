import logging

from src.reports.adapters.json import JsonReportAdapter
from src.reports.builders.json import TrackedArticlesJSONReportBuilder
from src.reports.filters.base import BaseReportFilter
from src.reports.transfer.report import Report
from src.services.dealer import DeallerWebService

from ._utils import report_to_update_report
from .base import BaseRepository


class DealerReportsRepository(BaseRepository):
    _service: DeallerWebService
    _builder: TrackedArticlesJSONReportBuilder
    _adapter: JsonReportAdapter

    def __init__(self, service: DeallerWebService,
                 builder: TrackedArticlesJSONReportBuilder = TrackedArticlesJSONReportBuilder,
                 reports_filter: BaseReportFilter = None,
                 adapter: JsonReportAdapter = JsonReportAdapter):
        super().__init__(service=service, builder=builder, reports_filter=reports_filter, adapter=adapter)

    async def get_all(self) -> Report:
        logging.debug("Call Dealer Repository Get All")

        result = await self._service.get()

        logging.debug("Dealer Get Request Completed")

        return self._builder(data=result,
                             filter_=self._filter,
                             adapter=self._adapter).report

    async def save(self, report: Report) -> None:
        logging.debug("Call Dealer Repository Save")

        await self._service.post(
            update_report=report_to_update_report(report=report)
        )

        logging.debug("Dealer Save Request Completed")
