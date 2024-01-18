from typing import TypeVar

from dataclasses import dataclass


ArticleCode = TypeVar("ArticleCode", bound=str)
LeftOverAmount = TypeVar("LeftOverAmount", bound=int)


@dataclass(frozen=True)
class Article:
    article: ArticleCode
    leftover: LeftOverAmount
