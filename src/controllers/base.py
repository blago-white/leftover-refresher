from abc import ABCMeta, abstractmethod
from typing import Any


class Controller(metaclass=ABCMeta):
    @abstractmethod
    def refresh(self):
        pass

    @abstractmethod
    def _get_difference(self):
        pass

    @abstractmethod
    def _commit_difference(self):
        pass