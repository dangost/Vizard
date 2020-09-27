from abc import abstractmethod


class BaseDatabase:

    games: list
    studios: list
    genres: list

    games_path: str = "games.json"
    studios_path: str = "studios.json"
    genres_path: str = "genres.json"

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def create_base(self, path: str):
        pass
