
from abc import ABCMeta, abstractmethod
from datetime import datetime


class AbstractBatch(metaclass=ABCMeta):

    @abstractmethod
    def fill(self, extractor):
        raise NotImplemented

    @abstractmethod
    def push(self, loader):
        raise NotImplemented


class AbstractExtractor(metaclass=ABCMeta):
    def __init__(self):
        self.extraction_timestamp: datetime or None = None
        self.record_source = None
        self.output = None

    @abstractmethod
    def _set_extraction_timestamp(self):
        raise NotImplementedError

    @abstractmethod
    def _set_record_source(self):
        raise NotImplementedError

    @abstractmethod
    def extract(self):
        raise NotImplementedError

    @abstractmethod
    def unify(self):
        raise NotImplementedError


class AbstractLoader(metaclass=ABCMeta):

    def __init__(self, **kwargs):

        self.output = None

    @abstractmethod
    def prepare(self, batch):
        raise NotImplementedError

    @abstractmethod
    def load(self):
        raise NotImplementedError
