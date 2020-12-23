from .model import Genre
from application.entities.abstract.base_repository import BaseRepository


class GenresRepository(BaseRepository):
    def get_all(self):
        return self.db.get_all(Genre)

    def get_id(self, item_id):
        genre = self.db.get_by_id(Genre, item_id)
        if genre is not None:
            return genre
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.genres:
            if condition(each):
                res.append(each)
        return res

    def add(self, genre: Genre):
        self.db.genres.append(genre)
        self.db.add(genre)
        return "OK"

    def replace(self, genre: Genre, genre_id):
        temp = self.get_id(genre_id)
        if temp == "No such Id":
            return temp
        self.db.update(Genre, Genre.genre_id, genre_id, genre)
        return "OK"

    def remove(self, genre_id: int):
        temp = self.get_id(genre_id)
        if temp == "No such Id":
            return temp
        self.db.delete(temp)
        return "OK"
