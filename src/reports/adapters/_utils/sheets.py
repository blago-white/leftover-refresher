from typing import Any

from src.config.settings import SupplierWebSettings
from src.reports.transfer import report


def row_to_article(row: tuple[Any]) -> report.Article:
    return report.Article(
        article=row[SupplierWebSettings.ARTICLE_CODE_COL_NUMBER],
        leftover=row[SupplierWebSettings.ARTICLE_LEFTOVER_COL_NUMBER]
    )
