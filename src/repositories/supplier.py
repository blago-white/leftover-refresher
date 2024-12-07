import logging

from src.reports.adapters.xls import XlsReportAdapter
from src.reports.builders.xls import TrackedArticlesXlsReportBuilder
from src.reports.filters.tracked import TrackedAtriclesFilter
from src.services.supplier import SupplierXLSReportService
from .base import BaseReadOnlyRepository


class SupplierReportsRepository(BaseReadOnlyRepository):
    _service: SupplierXLSReportService
    _builder: TrackedArticlesXlsReportBuilder
    _filter: TrackedAtriclesFilter
    _adapter: XlsReportAdapter

    def __init__(
            self, service: SupplierXLSReportService,
            builder: TrackedArticlesXlsReportBuilder = TrackedArticlesXlsReportBuilder,
            reports_filter: TrackedAtriclesFilter = TrackedAtriclesFilter,
            adapter: XlsReportAdapter = XlsReportAdapter):
        super().__init__(service=service, builder=builder,
                         reports_filter=reports_filter, adapter=adapter)

    async def get_all(self):
        logging.debug("Call Supplier Repository Get All")

        result = self._service.get()

        logging.debug("Supplier Get Request Completed")

        return self._builder(data=result,
                             filter_=self._filter,
                             adapter=self._adapter).report
