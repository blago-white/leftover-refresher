import io
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

from src.config.settings import SupplierWebSettings

from .base import BaseReportAdapter
from ._utils import utils


class XmlReportAdapter(BaseReportAdapter):
    """
    1. Перевести в IO
    2. Создать книгу / взять лист
    3. Отфильтровать значения
    4. Сериализировать значения в Report class
    """

    def data(self):
        work_sheet = self._get_work_sheet()

        tracked_articles = utils.extract_tracked_atricles(ws=work_sheet)

        return tracked_articles

    def _get_work_sheet(self) -> Worksheet:
        wb = openpyxl.load_workbook(
            _utils.get_io_from_bytes(content=self._raw_data)
        )

        return wb[wb.sheetnames[0]]
