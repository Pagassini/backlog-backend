from http.client import HTTPException
from typing import List
from exceptions.game_exceptions import GameAlreadyExistsException, GameNotFoundException
from exceptions.genre_exceptions import GenreNotFoundException
from exceptions.platform_exceptions import PlatformNotFoundException
from models.dtos.game_dto import GameCreateDTO, GameUpdateDTO
from models.game import GameModel, GameUpdateModel
from models.viewmodels.game_viewmodel import GameViewModel
from repositories.game_repository import GameRepository
from repositories.genre_repository import GenreRepository
from repositories.platform_repository import PlatformRepository


class GameService:
    
    @staticmethod
    async def create(db, game_dto: GameCreateDTO) -> GameViewModel:
        
        for platforms in game_dto.platforms:
            if not await PlatformRepository.exists(db, platforms):
                raise PlatformNotFoundException()
        
        for genres in game_dto.genres:
            if not await GenreRepository.exists(db, genres):
                raise GenreNotFoundException()
        
        if await GameRepository.title_exists(db, game_dto.title):
                raise GameAlreadyExistsException()
        
        game_model = GameModel(
            title=game_dto.title,
            description=game_dto.description,
            platforms=game_dto.platforms,
            genres=game_dto.genres,
            release_date=game_dto.release_date,
            developer=game_dto.developer,
            publisher=game_dto.publisher
        )
        
        created_game = await GameRepository.create(db, game_model)
        created_game['platforms'] = [platform for platform in created_game['platforms']]
        created_game['genres'] = [genre for genre in created_game['genres']]
        return GameViewModel(**created_game)

    
    @staticmethod
    async def find_all(db) -> List[GameViewModel]:

        games_cursor = await GameRepository.find_all(db)
        games = []
        for game in games_cursor:
            game_view_model = GameViewModel(**game)
            games.append(game_view_model)
        return games
    
    @staticmethod
    async def find_by_id(db, id: str) -> GameViewModel:

        if not await GameRepository.exists(db, id):
                raise GameNotFoundException()
        
        return await GameRepository.find_by_id(db, id)
    
    @staticmethod
    async def update(db, id: str, game_update_dto: GameUpdateDTO) -> GameViewModel:
        
        if not await GameRepository.exists(db, id):
            raise GameNotFoundException()

        for platform in game_update_dto.platforms:
            if not await PlatformRepository.exists(db, platform):
                raise PlatformNotFoundException()
        
        for genre in game_update_dto.genres:
            if not await GenreRepository.exists(db, genre):
                raise GenreNotFoundException()
        
        if await GameRepository.title_exists(db, game_update_dto.title):
            raise GameAlreadyExistsException()
            
        update_data = GameUpdateModel(
            title=game_update_dto.title,
            description=game_update_dto.description,
            platforms=game_update_dto.platforms,
            genres= game_update_dto.genres,
            release_date= game_update_dto.release_date,
            developer= game_update_dto.developer,
            publisher= game_update_dto.publisher
        )
        
        updated_game = await GameRepository.update(db, id, update_data)
        updated_game['platforms'] = [platforms for platforms in updated_game['platforms']]
        updated_game['genres'] = [genres for genres in updated_game['genres']]
        return GameViewModel(**updated_game)
    
    @staticmethod
    async def delete(db, id: str) -> bool:

        if not await GameRepository.exists(db, id):
            raise GameNotFoundException()
        
        deleted = await GameRepository.delete(db, id)
        return deleted