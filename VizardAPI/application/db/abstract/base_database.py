from abc import abstractmethod


class BaseDatabase:

    games: list
    studios: list
    genres: list

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def create_base(self, path: str):
        pass
