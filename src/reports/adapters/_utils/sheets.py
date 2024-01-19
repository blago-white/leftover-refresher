from typing import Iterable

from openpyxl.worksheet.worksheet import Worksheet

from src.config.settings import SupplierSettings
from src.reports.transfer import report


def row_to_article(row: tuple[str]) -> report.Article:
    return report.Article(
        article=row[SupplierSettings.ARTICLE_CODE_COL_NUMBER],
        leftover=row[SupplierSettings.ARTICLE_LEFTOVER_COL_NUMBER]
    )


def rows_to_report(rows: Iterable[tuple[str]]) -> report.Report:
    return report.Report(articles=list(map(row_to_article, rows)))


def extract_values_from_sheet(sheet: Worksheet) -> report.Report:
    return sheet.values
