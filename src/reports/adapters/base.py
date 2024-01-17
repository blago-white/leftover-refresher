from abc import ABCMeta, abstractmethod


class BaseAdapter:
    def __init__(self, data: bytes):
        pass

    @abstractmethod
    @property
    def data(self):
        #  returns, converted, python - friendly data
        pass
