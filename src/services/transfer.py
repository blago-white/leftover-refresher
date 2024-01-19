from dataclasses import dataclass

from src.reports.transfer.report import Report


@dataclass(frozen=True)
class ArticleLeftoversUpdateForm:
    article_id: str
    leftover: int


class UpdateReport(Report):
    articles: list[ArticleLeftoversUpdateForm]
