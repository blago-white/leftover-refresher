import io

from openpyxl.worksheet.worksheet import Worksheet

from src.reports.transfer import report


def extract_values_from_sheet(sheet: Worksheet) -> report.Report:
    return sheet.values


def get_io_from_bytes(content: bytes) -> io.BytesIO:
    return io.BytesIO(content)
