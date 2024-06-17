from http.client import HTTPException
from typing import List
from models.dtos.game_dto import GameCreateDTO, GameUpdateDTO
from models.game import GameModel, GameUpdateModel
from models.viewmodels.game_viewmodel import GameViewModel
from repositories.game_repository import GameRepository
from repositories.genre_repository import GenreRepository
from repositories.platform_repository import PlatformRepository


class GameService:
    
    @staticmethod
    async def create(db, game_dto: GameCreateDTO) -> GameViewModel:
        
        for platform_id in game_dto.platform:
            if not await PlatformRepository.exists(db, platform_id):
                raise HTTPException(status_code=400)
        
        for genre_id in game_dto.genre:
            if not await GenreRepository.exists(db, genre_id):
                raise HTTPException(status_code=400)
        
        game_model = GameModel(
            title=game_dto.title,
            description=game_dto.description,
            platform=game_dto.platform,
            genre=game_dto.genre,
            release_date=game_dto.release_date,
            developer=game_dto.developer,
        )
        
        created_game = await GameRepository.create(db, game_model)
        created_game['platform'] = [platform_id for platform_id in created_game['platform']]
        created_game['genre'] = [genre_id for genre_id in created_game['genre']]
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
        return await GameRepository.find_by_id(db, id)
    
    @staticmethod
    async def update(db, id: str, game_update_dto: GameUpdateDTO) -> GameViewModel:
        
        for platform_id in game_update_dto.platform:
            if not await PlatformRepository.exists(db, platform_id):
                raise HTTPException(status_code=400)
        
        for genre_id in game_update_dto.genre:
            if not await GenreRepository.exists(db, genre_id):
                raise HTTPException(status_code=400)
            
        update_data = GameUpdateModel(
            title=game_update_dto.title,
            description=game_update_dto.description,
            platform=game_update_dto.platform,
            genre= game_update_dto.genre,
            release_date= game_update_dto.release_date,
            developer= game_update_dto.developer
        )
        
        updated_game = await GameRepository.update(db, id, update_data)
        updated_game['platform'] = [platform_id for platform_id in updated_game['platform']]
        updated_game['genre'] = [genre_id for genre_id in updated_game['genre']]
        return GameViewModel(**updated_game)
    
    @staticmethod
    async def delete(db, id: str) -> bool:
        deleted = await GameRepository.delete(db, id)
        return deleted