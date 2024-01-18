from .base import BaseReportBuilder
from ..adapters.xls import XlsReportAdapter
from ..filters.tracked import TrackedAtriclesFilter


class TrackedArticlesReportBuilder(BaseReportBuilder):
    def __init__(self, data: bytes,
                 filter_: TrackedAtriclesFilter = TrackedAtriclesFilter,
                 adapter: XlsReportAdapter = XlsReportAdapter):
        super().__init__(data=data, filter_=filter_, adapter=adapter)

    @property
    def report(self):
        report = self._adapter(self._data).data

        return self._filter(report).result
