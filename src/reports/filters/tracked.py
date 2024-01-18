from src.config.settings import SupplierWebSettings

from ..transfer.report import Report

from .base import BaseReportFilter


class TrackedAtriclesFilter(BaseReportFilter):
    _result: Report = None

    def __init__(self, report: Report):
        self._extract_tracked_atricles(report=report)

    @property
    def result(self) -> Report:
        return self._result

    def _extract_tracked_atricles(self, report: Report) -> None:
        result = Report()

        for article in report.articles:
            if article.article in SupplierWebSettings.TRACKED_ARTICLES:
                result.add(article=article)

        self._result = result
