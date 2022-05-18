from core.abstract import AbstractLoader


class DatabaseLoader(AbstractLoader):

    def __init__(self):
        super().__init__()

    def prepare(self, batch):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError


class FileLoader(AbstractLoader):

    def __init__(self, uri):
        super().__init__()
        self.uri: str = uri

    def prepare(self, batch):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError
