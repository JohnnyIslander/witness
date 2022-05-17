from core.abstract import AbstractLoader


class DatabaseLoader(AbstractLoader):

    def __init__(self):
        super().__init__()

    def prepare(self, batch):
        pass

    def load(self):
        pass


class FileLoader(AbstractLoader):

    def __init__(self):
        super().__init__()

    def prepare(self, batch):
        pass

    def load(self):
        pass
