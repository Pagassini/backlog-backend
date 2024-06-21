from typing import List
from exceptions.backlog_exceptions import BacklogNotFoundException
from exceptions.game_exceptions import GameNotFoundException
from exceptions.user_exceptions import UserNotFoundException
from models.backlog import BacklogModel, BacklogUpdateModel
from models.dtos.backlog_dto import BacklogCreateDTO, BacklogUpdateDTO
from models.viewmodels.backlog_viewmodel import BacklogViewModel
from repositories.backlog_repository import BacklogRepository
from repositories.game_repository import GameRepository
from repositories.user_repository import UserRepository


class BacklogService:

    @staticmethod
    async def create(db, backlog_dto: BacklogCreateDTO) -> BacklogViewModel:

        if not await GameRepository.exists(db, backlog_dto.game_id):
            raise GameNotFoundException()
        
        if not await UserRepository.exists(db, backlog_dto.user_id):
            raise UserNotFoundException()
        
        backlog_model = BacklogModel(
            game_id=backlog_dto.game_id,
            user_id=backlog_dto.user_id,
            status=backlog_dto.status
        )

        created_backlog = await BacklogRepository.create(db, backlog_model)
        return BacklogViewModel(**created_backlog)
    
    @staticmethod
    async def find_by_user(db, id: str) -> List[BacklogViewModel]:

        if not await UserRepository.exists(db, id):
            raise UserNotFoundException()

        backlog_cursor = await BacklogRepository.find_by_user(db, id)
        backlogs = []
        for backlog in backlog_cursor:
            backlog_view_model = BacklogViewModel(**backlog)
            backlogs.append(backlog_view_model)
        return backlogs
    
    @staticmethod
    async def update(db, id: str, backlog_update_dto: BacklogUpdateDTO) -> BacklogViewModel:
                    
        if not await BacklogRepository.exists(db, id):
            raise BacklogNotFoundException()
        
        update_data = BacklogUpdateModel(
            status=backlog_update_dto.status
        )
        
        updated_backlog = await BacklogRepository.update(db, id, update_data)
        return BacklogViewModel(**updated_backlog)
    
    @staticmethod
    async def delete(db, id: str) -> bool:

        if not await BacklogRepository.exists(db, id):
            raise BacklogNotFoundException()
        
        deleted = await BacklogRepository.delete(db, id)
        return deleted
    


