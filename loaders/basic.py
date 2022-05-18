from core.abstract import AbstractLoader


class DatabaseLoader(AbstractLoader):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def prepare(self, batch):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class FileLoader(AbstractLoader):

    def __init__(self, uri, **kwargs):
        self.uri: str = uri
        super().__init__(**kwargs)

    def prepare(self, batch):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError
