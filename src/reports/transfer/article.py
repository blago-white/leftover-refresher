from dataclasses import dataclass
from typing import TypeVar

from src.config.settings import SupplierSettings

ArticleCode = TypeVar("ArticleCode", bound=str)
LeftOverAmount = TypeVar("LeftOverAmount", bound=int)


@dataclass
class Article:
    article: ArticleCode
    leftover: LeftOverAmount

    def __post_init__(self):
        try:
            self.leftover = SupplierSettings.ARTICLE_LEFTOVER_VALUE_TYPE(
                self.leftover
            )

            self.leftover = SupplierSettings.ARTICLE_LEFTOVER_FILTER(
                self.leftover
            )

        except (ValueError, TypeError):
            pass

    def __eq__(self, other):
        if type(other) is not self.__class__:
            return False

        return self.leftover == other.leftover
