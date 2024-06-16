from typing import List
from models.dtos.game_dto import GameCreateDTO, GameUpdateDTO
from models.game import GameModel
from models.viewmodels.game_viewmodel import GameViewModel
from repositories.game_repository import GameRepository


class GameService:
    
    @staticmethod
    async def create(db, game_dto: GameCreateDTO) -> GameViewModel:
        game_model = GameModel(
            title=game_dto.title,
            description=game_dto.description,
            platform=game_dto.platform,
            genre=game_dto.genre,
            release_date=game_dto.release_date,
            developer=game_dto.developer,
        )
        
        created_game = await GameRepository.create(db, game_model)
        return GameViewModel(**created_game)

    
    @staticmethod
    async def find_all(db) -> List[GameViewModel]:
        games_cursor = db['games'].find()
        games = []
        for game in games_cursor:
            game_view_model = GameViewModel(**game)
            games.append(game_view_model)
        return games
    
    @staticmethod
    async def update(db, game_id: str, game_update_dto: GameUpdateDTO) -> GameViewModel:
        update_data = GameModel(
            title=game_update_dto.title,
            description=game_update_dto.description,
            platform=game_update_dto.description,
            genre= game_update_dto.genre,
            release_date= game_update_dto.release_date,
            developer= game_update_dto.developer
        )
        
        updated_game = await GameRepository.update(db, game_id, update_data)
        return GameViewModel(**updated_game)
    
    @staticmethod
    async def delete(db, game_id: str) -> bool:
        deleted = await GameRepository.delete(db, game_id)
        return deleted