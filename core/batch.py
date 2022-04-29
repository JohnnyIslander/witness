
from datetime import datetime


class Batch(object):

    __slots__ = ('data', 'meta')

    def __init__(self, batch):

        self.data = batch['data']
        self.meta = batch['meta']

    def persist(self, uri):
        pass

    def restore(self, uri):
        pass
