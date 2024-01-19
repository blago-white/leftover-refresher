from src.config.settings import SupplierWebSettings
from .base import BaseReportFilter
from ..transfer.report import Report


class TrackedAtriclesFilter(BaseReportFilter):
    _result: Report = None

    def __init__(self, report: Report):
        self._extract_tracked_atricles(report=report)

    @property
    def result(self) -> Report:
        return self._result

    def _extract_tracked_atricles(self, report: Report) -> None:
        self._result = Report(articles=[
            article
            for article in report.articles
            if article.article in SupplierWebSettings.TRACKED_ARTICLES
        ])
