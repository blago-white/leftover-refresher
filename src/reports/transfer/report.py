from dataclasses import dataclass, field

from .article import Article


@dataclass
class Report:
    articles: list[Article] = field(default_factory=list)

    def __bool__(self):
        return bool(self.articles)

    def add(self, article: Article):
        self.articles.append(article)

    @property
    def sorted(self) -> list[Article]:
        return sorted(self.articles, key=lambda article: article.article)


@dataclass
class ReportsPair:
    slave_report: Report
    master_report: Report

    @property
    def difference(self) -> Report:
        return Report(
            articles=[articles[0]
                      for articles in zip(self.master_report.sorted,
                                          self.slave_report.sorted,
                                          strict=True)
                      if articles[0] != articles[1]]
        )
