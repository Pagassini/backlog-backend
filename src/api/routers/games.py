from typing import List
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models.dtos.game_dto import GameCreateDTO, GameUpdateDTO
from models.game import GameModel, GameUpdateModel
from models.viewmodels.game_viewmodel import GameViewModel
from services.game_service import GameService


router = APIRouter()

@router.post("/", response_model=GameViewModel)
async def create_game(game: GameCreateDTO, request: Request):
    return await GameService.create(request.app.database, game)

@router.put("/{id}", response_model=GameViewModel)
async def update_game(id: str, game: GameUpdateDTO, request: Request):
    return await GameService.update(request.app.database, id, game)