from models.genre import GenreModel


class GenreRepository:
    
    @staticmethod
    async def find_all(db):
        genres = db["genres"].find()
        return genres
    
    @staticmethod
    async def exists(db, id: str) -> bool:
        return db["genres"].find_one({"_id": id})
    
    @staticmethod
    async def create(db, genre: GenreModel):
        genre_dict = genre.dict(by_alias=True)
        genre_dict["_id"] = str(genre_dict["_id"])
        result = db['genres'].insert_one(genre_dict)
        genre_dict['_id'] = str(result.inserted_id)
        return genre_dict