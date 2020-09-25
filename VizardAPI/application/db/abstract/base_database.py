from abc import abstractmethod


class BaseDatabase:
    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass


