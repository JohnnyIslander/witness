
from abc import ABCMeta, abstractmethod


class AbstractLoader(metaclass=ABCMeta):

    def __init__(self):

        self.output = None

    @abstractmethod
    def prepare(self, batch):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError


class DatabaseLoader(AbstractLoader):

    def __init__(self):
        super().__init__()

    def prepare(self, batch):
        pass

    def load(self):
        pass
