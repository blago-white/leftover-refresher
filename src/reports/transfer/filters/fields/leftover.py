from typing import Any

from .base import BaseLeftoverNumberFieldFilter


class LeftoverMinValueFieldFilter(BaseLeftoverNumberFieldFilter):
    def __call__(self, value: Any) -> Any:
        return max(self._value, value)


class LeftoverMaxValueFieldFilter(BaseLeftoverNumberFieldFilter):
    def __call__(self, value: Any) -> Any:
        return min(value, self._value)
