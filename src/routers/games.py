from typing import List
from fastapi import APIRouter, Request
from models.dtos.game_dto import GameCreateDTO, GameUpdateDTO
from models.viewmodels.game_viewmodel import GameViewModel
from services.game_service import GameService


router = APIRouter()

@router.post("", response_model=GameViewModel)
async def post(game: GameCreateDTO, request: Request):
    return await GameService.create(request.app.database, game)

@router.put("/{id}", response_model=GameViewModel)
async def update(id: str, game: GameUpdateDTO, request: Request):
    return await GameService.update(request.app.database, id, game)

@router.delete("/{id}")
async def delete(id: str, request: Request):
    return await GameService.delete(request.app.database, id)

@router.get("", response_model=List[GameViewModel])
async def get(request: Request):
    return await GameService.find_all(request.app.database)

@router.get("/{id}")
async def get(id: str, request: Request):
    return await GameService.find_by_id(request.app.database)