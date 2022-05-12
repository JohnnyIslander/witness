
from abc import ABCMeta, abstractmethod
from datetime import datetime


class AbstractExtractor(metaclass=ABCMeta):
    def __init__(self):
        self.extraction_timestamp: datetime or None = None
        self.output = None

    @abstractmethod
    def _set_extraction_timestamp(self):
        raise NotImplementedError

    @abstractmethod
    def extract(self):
        raise NotImplementedError

    @abstractmethod
    def unify(self):
        raise NotImplementedError


class FileExtractor(AbstractExtractor):

    def __init__(self, uri: str, params: dict or None = None):
        super().__init__()
        self.uri = uri
        self.params = params
        self.name = 'unnamed'

        data: dict

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def extract(self):
        self._set_extraction_timestamp()

    def unify(self):
        pass


class DatabaseExtractor(AbstractExtractor):

    def __init__(self):
        super().__init__()

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def extract(self):
        self._set_extraction_timestamp()

    def unify(self):
        pass
