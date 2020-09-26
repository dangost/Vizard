from abc import abstractmethod


class BaseDatabase:

    games_path: str = "games.json"
    studios_path: str = "studios.json"
    genres_path: str = "genres.json"

    @abstractmethod
    def create_base(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass


