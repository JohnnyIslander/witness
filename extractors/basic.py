from datetime import datetime
from core.abstract import AbstractExtractor


class FileExtractor(AbstractExtractor):

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
