import functools
from typing import Iterable, Any

from .fields.base import BaseFieldFilter


class BaseArticleLeftoverFilter:
    _filters: dict[str, BaseFieldFilter]

    def __init__(self, filters: Iterable[BaseFieldFilter]):
        self._filters = filters

    def __call__(self, value: Any) -> Any:
        return functools.reduce(lambda x, y: y(x), self._filters, value)
