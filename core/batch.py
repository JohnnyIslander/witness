
from datetime import datetime


class Batch(object):

    __slots__ = ('data', 'source', 'extraction', 'name')

    def __init__(self, data, source: str, extraction: datetime, name: str = 'unnamed'):

        self.data = data
        self.source = source
        self.extraction = extraction
        self.name = name

    def persist(self, uri):
        pass

    def restore(self, uri):
        pass
