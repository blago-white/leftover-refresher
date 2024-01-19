from dataclasses import dataclass, field

from .article import Article


@dataclass
class Report:
    articles: list[Article] = field(default_factory=list)

    def add(self, article: Article):
        self.articles.append(article)


@dataclass
class ReportsPair:
    slave_report: Report
    master_report: Report

    @property
    def difference(self) -> Report:
        return Report(
            articles=[articles[0]
                      for articles in zip(self.master_report.articles,
                                          self.slave_report.articles,
                                          strict=True)
                      if articles[0] != articles[1]]
        )
