from src.reports.builders.articles import TrackedArticlesReportBuilder
from src.reports.adapters.xls import XlsReportAdapter
from src.services.supplier import SupplierLeftoversWebService

from .base import BaseReadOnlyRepository


class SupplierReportsRepository(BaseReadOnlyRepository):
    _service: SupplierLeftoversWebService
    _builder: TrackedArticlesReportBuilder
    _adapter: XlsReportAdapter

    def __init__(self, service: SupplierLeftoversWebService,
                 builder: TrackedArticlesReportBuilder = TrackedArticlesReportBuilder,
                 adapter: XlsReportAdapter = XlsReportAdapter):
        super().__init__(service=service, builder=builder, adapter=adapter)

    async def get_all(self):
        result = await self._service.get()

        return self._builder(data=result, adapter=self._adapter).report
