
from datetime import datetime


class Extractor(object):

    def __init__(self, uri: str, params: dict or None = None):

        self.uri = uri
        self.params = params
        self.name = 'unnamed'
        self.extraction_timestamp: datetime or None = None

        data: dict

    def extract(self):
        pass



