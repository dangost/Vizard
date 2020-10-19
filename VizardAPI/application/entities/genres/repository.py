from .model import Genre
from .schema import GenresSchema


class GenresRepository:
    def __init__(self, base):
        self.db = base

    def get_all_genres(self):
        return self.db.genres

    def get_id_genre(self, item_id) -> Genre or str:
        for each in self.db.genres:
            if each.genre_id == item_id:
                return each
        return "No such Id"

    def post_genre(self, json_data: dict):
        genre = GenresSchema(many=False).load(json_data)
        if type(genre) is not Genre:
            return "Invalid data"
        self.db.genres.append(genre)
        self.db.save()
        return "OK"

    def put_genre(self, genre_id: int, json_data: dict):
        for i in range(len(self.db.genres)):
            if self.db.genres[i].genre_id == genre_id:
                genre = GenresSchema(many=False).load(json_data)
                if type(genre) is Genre:
                    return "Invalid data"
                self.db.genres[i] = genre
                self.db.save()
                return "OK"
        return "No such Id"

    def delete_genre(self, item_id: int):
        for each in self.db.genres:
            if each.genre_id == item_id:
                self.db.genres.remove(each)
                self.db.save()
                return "OK"
        return "No such Id"
