
#  Copyright (c) 2022. Eugene Popov
#  All rights reserved.

from core.abstract import AbstractBatch


class Batch(AbstractBatch):
    """
    Central class of entire lib.
    Able to store standardized data structure
    containing data in form of records and metadata dictionary.
    """

    __slots__ = ('data', 'meta')

    def __init__(self):

        self.data: list = []
        self.meta: dict = {}

    def fill(self, extractor):
        output = extractor.extract().unify().output
        setattr(self, 'data', output['data'])
        setattr(self, 'meta', output['meta'])
        return self

    def push(self, loader):
        loader.prepare(self).load()
        return self

    def persist(self, uri):
        raise NotImplementedError

    def restore(self, uri):
        raise NotImplementedError
