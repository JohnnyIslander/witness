
from datetime import datetime


class Batch:

    __slots__ = ('data', 'meta')

    def __init__(self, struct: dict):

        self.data: list = struct['data']
        self.meta: dict = struct['meta']

    def persist(self, uri):
        pass

    def restore(self, uri):
        pass
