from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, db):
        self.db = db

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_id(self, item_id):
        pass

    @abstractmethod
    def find(self, condition):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def replace(self, item, item_id):
        pass

    @abstractmethod
    def remove(self, item_id):
        pass
