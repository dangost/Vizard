from abc import abstractmethod


class BaseDatabase:

    games: list
    studios: list
    genres: list

    users: list
    users_to_games: list
    users_to_rates: list

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self):
        pass
