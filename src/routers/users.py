
from typing import List
from fastapi import APIRouter, Request

from models.dtos.user_dto import UserCreateDTO, UserUpdateDTO
from models.viewmodels.user_viewmodel import UserViewModel
from services.user_service import UserService


router = APIRouter()

@router.post("", response_model=UserViewModel)
async def post(game: UserCreateDTO, request: Request):
    return await UserService.create(request.app.database, game)

@router.put("/{id}", response_model=UserViewModel)
async def update(id: str, game: UserUpdateDTO, request: Request):
    return await UserService.update(request.app.database, id, game)

@router.delete("/{id}")
async def delete(id: str, request: Request):
    return await UserService.delete(request.app.database, id)

@router.get("", response_model=List[UserViewModel])
async def get(request: Request):
    return await UserService.find_all(request.app.database)