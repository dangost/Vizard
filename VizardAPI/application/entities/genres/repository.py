from .model import Genre
from application.entities.abstract.base_repository import BaseRepository


class GenresRepository(BaseRepository):
    def get_all(self):
        return self.db.genres

    def get_id(self, item_id):
        for each in self.db.genres:
            if each.genre_id == item_id:
                return each
        return "No such Id"

    def find(self, condition):
        res = []
        for each in self.db.genres:
            if condition(each):
                res.append(each)
        return res

    def add(self, genre: Genre):
        self.db.genres.append(genre)
        self.db.save()
        return "OK"

    def replace(self, genre: Genre, genre_id):
        for i in range(len(self.db.genres)):
            if self.db.genres[i].genre_id == genre_id:
                self.db.genres[i] = genre
                self.db.save()
                return "OK"
        return "No such Id"

    def remove(self, genre_id: int):
        for each in self.db.genres:
            if each.genre_id == genre_id:
                self.db.genres.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
