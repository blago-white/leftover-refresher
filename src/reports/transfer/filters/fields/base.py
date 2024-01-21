from abc import ABCMeta, abstractmethod
from typing import Any


class BaseFieldFilter(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, value: Any) -> Any:
        pass


class BaseLeftoverNumberFieldFilter(BaseFieldFilter, metaclass=ABCMeta):
    _value: int

    def __init__(self, value: int):
        self._value = value
