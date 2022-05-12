
from abc import ABCMeta, abstractmethod


class AbstractLoader(metaclass=ABCMeta):

    def __init__(self):

        self.input = None

    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError


class DatabaseLoader(AbstractLoader):

    def __init__(self):
        super().__init__()

    def prepare(self):
        pass

    def load(self):
        pass