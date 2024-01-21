from typing import Iterable

from src.tracked.utils import get_tracked_articles_ids
from .base import BaseReportFilter
from ..transfer.report import Report


class TrackedAtriclesFilter(BaseReportFilter):
    _tracked: Iterable[str]

    def __init__(self, tracked_articles: Iterable[str] = None):
        if tracked_articles is None:
            tracked_articles = get_tracked_articles_ids()

        self._tracked = tracked_articles

    def __call__(self, report: Report) -> Report:
        return self._extract_tracked_atricles(report=report)

    def _extract_tracked_atricles(self, report: Report) -> Report:
        return Report(articles=[
            article
            for article in report.articles
            if article.article in self._tracked
        ])
