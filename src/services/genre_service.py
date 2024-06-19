from typing import List
from exceptions.genre_exceptions import GenreAlreadyExistsException
from models.dtos.genre_dto import GenreCreateDTO
from models.genre import GenreModel
from models.viewmodels.genre_viewmodel import GenreViewModel
from repositories.genre_repository import GenreRepository


class GenreService:
    
    @staticmethod
    async def create(db, genre_dto: GenreCreateDTO) -> GenreViewModel:
        
        if await GenreRepository.name_exists(db, genre_dto.name):
            raise GenreAlreadyExistsException()
        
        genre_model = GenreModel(
            name=genre_dto.name
        )
        
        created_genre = await GenreRepository.create(db, genre_model)
        return GenreViewModel(**created_genre)
    
    @staticmethod
    async def find_all(db) -> List[GenreViewModel]:
        genres_cursor = await GenreRepository.find_all(db)
        genres = []
        for genre in genres_cursor:
            genre_view_model = GenreViewModel(**genre)
            genres.append(genre_view_model)
        return genres