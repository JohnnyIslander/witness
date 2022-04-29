
from datetime import datetime


class Batch(object):

    __slots__ = ('data', 'meta')

    def __init__(self, src: dict):

        self.data: list = src['data']
        self.meta: dict = src['meta']

    def persist(self, uri):
        pass

    def restore(self, uri):
        pass
