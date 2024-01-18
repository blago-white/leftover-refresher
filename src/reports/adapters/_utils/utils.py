import io

from openpyxl.worksheet.worksheet import Worksheet
from typing import Iterable

from src.reports.transfer import report
from src.config.settings import SupplierWebSettings

from .sheets import row_to_article


def extract_tracked_atricles(ws: Worksheet) -> report.Report:
    result = report.Report()

    for row in ws:
        row = row_to_article(row)
        if row.article in SupplierWebSettings.TRACKED_ARTICLES:
            result.add(article=row)

    return result


def get_io_from_bytes(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)
