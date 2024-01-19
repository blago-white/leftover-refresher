from src.reports.adapters.xls import XlsReportAdapter
from src.reports.builders.articles import TrackedArticlesReportBuilder
from src.reports.filters.tracked import TrackedAtriclesFilter
from src.services.supplier import SupplierLeftoversWebService
from .base import BaseReadOnlyRepository


class SupplierReportsRepository(BaseReadOnlyRepository):
    _service: SupplierLeftoversWebService
    _builder: TrackedArticlesReportBuilder
    _filter: TrackedAtriclesFilter
    _adapter: XlsReportAdapter

    def __init__(self, service: SupplierLeftoversWebService,
                 builder: TrackedArticlesReportBuilder = TrackedArticlesReportBuilder,
                 reports_filter: TrackedAtriclesFilter = TrackedAtriclesFilter,
                 adapter: XlsReportAdapter = XlsReportAdapter):
        super().__init__(service=service, builder=builder, reports_filter=reports_filter, adapter=adapter)

    async def get_all(self):
        result = await self._service.get()

        return self._builder(data=result, filter_=self._filter, adapter=self._adapter).report
