from src.reports.transfer.report import Report

from ._utils.json import json_to_report
from .base import BaseReportAdapter


class JsonReportAdapter(BaseReportAdapter):
    @property
    def data(self) -> Report:
        return json_to_report(json=self._raw_data)
