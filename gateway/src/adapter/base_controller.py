from abc import ABC


class BaseController(ABC):
    def start(self):
        raise NotImplementedError
