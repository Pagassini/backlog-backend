from typing import List
from exceptions.user_exceptions import EmailAlreadyExistsException, UserNameAlreadyExistsException
from models.dtos.user_dto import UserCreateDTO, UserUpdateDTO
from models.user import UserModel, UserUpdateModel
from models.viewmodels.user_viewmodel import UserViewModel
from repositories.user_repository import UserRepository


class UserService:
    
    @staticmethod
    async def create(db, user_dto: UserCreateDTO) ->  UserViewModel:
        
        if await UserRepository.username_exists(db, user_dto.username):
            raise UserNameAlreadyExistsException()
        
        if await UserRepository.email_exists(db, user_dto.email):
            raise EmailAlreadyExistsException()
        
        user_model = UserModel(
            username=user_dto.username,
            email=user_dto.email,
            password=user_dto.password
        )
        
        created_user = await UserRepository.create(db, user_model)
        return UserViewModel(**created_user)
    
    @staticmethod
    async def find_all(db) -> List[UserViewModel]:
        users_cursor = await UserRepository.find_all(db)
        users= []
        for user in users_cursor:
            user_view_model = UserViewModel(**user)
            users.append(user_view_model)
        return users
    
    @staticmethod
    async def update(db, id: str, user_update_dto: UserUpdateDTO) -> UserViewModel:
        
        if await UserRepository.username_exists(db, user_update_dto.username):
            raise UserNameAlreadyExistsException()
        
        if await UserRepository.email_exists(db, user_update_dto.email):
            raise EmailAlreadyExistsException()
        
        update_data = UserUpdateModel(
            email=user_update_dto.email,
            password=user_update_dto.password,
            username=user_update_dto.username
        )
        
        updated_user = await UserRepository.update(db, id, update_data)
        return UserViewModel(**updated_user)
    
    @staticmethod
    async def delete(db, id: str) -> bool:
        deleted = await UserRepository.delete(db, id)
        return deleted