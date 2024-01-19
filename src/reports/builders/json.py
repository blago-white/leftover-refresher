from .base import DefaultReportBuilder
from ..adapters.json import JsonReportAdapter
from ..filters.base import BaseReportFilter


class TrackedArticlesJSONReportBuilder(DefaultReportBuilder):
    def __init__(self, data: bytes,
                 filter_: BaseReportFilter = None,
                 adapter: JsonReportAdapter = JsonReportAdapter):
        super().__init__(data=data, filter_=filter_, adapter=adapter)
