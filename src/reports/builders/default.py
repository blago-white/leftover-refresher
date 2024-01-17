from .base import BaseReportBuilder
from ..adapters.base import BaseAdapter


class DefaultReportBuilder(BaseReportBuilder):
    _data: bytes
    _adapter: BaseAdapter

    def __init__(self, data: bytes, adapter: BaseAdapter):
        self._data = data
        self._adapter = adapter

    @property
    def report(self):
        return self.adapter(self._data)
