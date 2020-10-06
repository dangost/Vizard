from .model import Genre
from .schema import GenresSchema
from application.app import base


class GenresRepository:
    @staticmethod
    def get_all_genres():
        return base.genres

    @staticmethod
    def get_id_genre(item_id) -> Genre or str:
        for each in base.genres:
            if each.genre_id == item_id:
                return each
        return "No such Id"

    @staticmethod
    def post_genre(json_data: dict):
        genre = GenresSchema(many=False).load(json_data)
        if type(genre) is not Genre:
            return "Invalid data"
        base.genres.append(genre)
        base.save()
        return "OK"

    @staticmethod
    def put_genre(genre_id: int, json_data: dict):
        for i in range(len(base.genres)):
            if base.genres[i].genre_id == genre_id:
                genre = GenresSchema(many=False).load(json_data)
                if type(genre) is Genre:
                    return "Invalid data"
                base.genres[i] = genre
                base.save()
                return "OK"
        return "No such Id"

    @staticmethod
    def delete_genre(item_id: int):
        for each in base.genres:
            if each.genre_id == item_id:
                base.genres.remove(each)
                base.save()
                return "OK"
        return "No such Id"
