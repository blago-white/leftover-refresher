from src.config.settings import DealerSettings
from src.reports.transfer.report import Report
from src.reports.transfer.article import Article
from src.services.transfer import UpdateReport, ArticleLeftoversUpdateForm


def report_to_update_report(report: Report) -> UpdateReport:
    return UpdateReport(
        list(map(_get_update_form, report.articles))
    )


def _get_update_form(article: Article) -> ArticleLeftoversUpdateForm:
    return ArticleLeftoversUpdateForm(
        article_id=article.article,
        leftover=article.leftover
    )
