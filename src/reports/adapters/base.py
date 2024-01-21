from abc import ABCMeta, abstractmethod


class BaseReportAdapter(metaclass=ABCMeta):
    _raw_data: bytes

    def __init__(self, raw_data: bytes):
        self._raw_data = raw_data

    @property
    @abstractmethod
    def data(self):
        pass
