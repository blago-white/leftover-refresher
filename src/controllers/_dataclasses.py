from dataclasses import dataclass

from src.reports.builders.base import BaseReportBuilder


@dataclass
class ReportBuildersPair:
    slave: BaseReportBuilder
    master: BaseReportBuilder
