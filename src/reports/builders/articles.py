from .base import BaseReportBuilder
from ..adapters.xls import XlsReportAdapter
from ..filters.tracked import TrackedAtriclesFilter
from ..transfer.report import Report


class TrackedArticlesReportBuilder(BaseReportBuilder):
    def __init__(self, data: bytes,
                 filter_: TrackedAtriclesFilter = TrackedAtriclesFilter,
                 adapter: XlsReportAdapter = XlsReportAdapter):
        super().__init__(data=data, filter_=filter_, adapter=adapter)

    @property
    def report(self) -> Report:
        report = self._adapter(self._data).data

        return self._get_filtered(report=report)

    def _get_filtered(self, report: Report) -> Report:
        if self._filter:
            return self._filter(report).result

        return report
