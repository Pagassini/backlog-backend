


from typing import List
from fastapi import APIRouter, Request

from models.dtos.genre_dto import GenreCreateDTO
from models.viewmodels.genre_viewmodel import GenreViewModel
from services.genre_service import GenreService


router = APIRouter()

@router.post("", response_model=GenreViewModel)
async def post(genre: GenreCreateDTO, request: Request):
    return await GenreService.create(request.app.database, genre)

@router.get("", response_model=List[GenreViewModel])
async def get(request: Request):
    return await GenreService.find_all(request.app.database)