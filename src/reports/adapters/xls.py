import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

from src.reports.transfer.report import Report
from ._utils import sheets, utils
from .base import BaseReportAdapter


class XlsReportAdapter(BaseReportAdapter):
    @property
    def data(self) -> Report:
        work_sheet = self._get_work_sheet()

        work_sheet_values = sheets.extract_values_from_sheet(sheet=work_sheet)

        return sheets.rows_to_report(rows=work_sheet_values)

    def _get_work_sheet(self) -> Worksheet:
        wb = openpyxl.load_workbook(
            utils.get_io_from_bytes(content=self._raw_data)
        )

        return wb[wb.sheetnames[0]]
