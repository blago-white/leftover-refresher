from dataclasses import dataclass, field

from .article import Article


@dataclass
class Report:
    articles: list[Article] = field(default_factory=list)

    def add(self, article: Article):
        self.articles.append(article)
