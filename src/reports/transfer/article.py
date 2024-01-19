from dataclasses import dataclass
from typing import TypeVar

from src.config.settings import SupplierWebSettings


ArticleCode = TypeVar("ArticleCode", bound=str)
LeftOverAmount = TypeVar("LeftOverAmount", bound=int)


@dataclass
class Article:
    article: ArticleCode
    leftover: LeftOverAmount

    def __post_init__(self):
        try:
            self.leftover = SupplierWebSettings.ARTICLE_LEFTOVER_VALUE_TYPE(
                self.leftover
            )
        except (ValueError, TypeError):
            pass
