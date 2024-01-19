from .base import DefaultReportBuilder

from ..adapters.xls import XlsReportAdapter
from ..filters.tracked import TrackedAtriclesFilter


class TrackedArticlesXlsReportBuilder(DefaultReportBuilder):
    def __init__(self, data: bytes,
                 filter_: TrackedAtriclesFilter = TrackedAtriclesFilter,
                 adapter: XlsReportAdapter = XlsReportAdapter):
        super().__init__(data=data, filter_=filter_, adapter=adapter)
