
from abc import ABCMeta, abstractmethod
from datetime import datetime


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


class FileExtractor(AbstractExtractor):

    def __init__(self):
        super().__init__()

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def _set_record_source(self):
        pass

    def extract(self):
        self._set_extraction_timestamp()

    def unify(self):
        pass


class DatabaseExtractor(AbstractExtractor):

    def __init__(self):
        super().__init__()

    def _set_extraction_timestamp(self):
        setattr(self, 'extraction_timestamp', datetime.now())

    def _set_record_source(self):
        pass

    def extract(self):
        self._set_extraction_timestamp()
        self._set_record_source()

    def unify(self):
        pass
