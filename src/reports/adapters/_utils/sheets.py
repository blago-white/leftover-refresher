from typing import Iterable

from src.config.settings import SupplierWebSettings
from src.reports.transfer import report


def row_to_article(row: tuple[str]) -> report.Article:
    return report.Article(
        article=row[SupplierWebSettings.ARTICLE_CODE_COL_NUMBER],
        leftover=row[SupplierWebSettings.ARTICLE_LEFTOVER_COL_NUMBER]
    )


def rows_to_report(rows: Iterable[tuple[str]]) -> report.Report:
    return report.Report(articles=list(map(row_to_article, rows)))
