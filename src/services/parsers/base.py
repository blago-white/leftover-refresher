from abc import ABCMeta, abstractmethod


class BaseStateParser(metaclass=ABCMeta):
    @property
    @abstractmethod
    def state(self):
        pass
