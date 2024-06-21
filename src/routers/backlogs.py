from typing import List
from fastapi import APIRouter, Request
from models.dtos.backlog_dto import BacklogCreateDTO, BacklogUpdateDTO
from models.viewmodels.backlog_viewmodel import BacklogViewModel
from services.backlog_service import BacklogService


router = APIRouter()

@router.post("", response_model=BacklogViewModel)
async def post(backlog: BacklogCreateDTO, request: Request):
    return await BacklogService.create(request.app.database, backlog)

@router.put("/{id}", response_model=BacklogViewModel)
async def update(id: str, game: BacklogUpdateDTO, request: Request):
    return await BacklogService.update(request.app.database, id, game)

@router.delete("/{id}")
async def delete(id: str, request: Request):
    return await BacklogService.delete(request.app.database, id)

@router.get("/{id}", response_model=List[BacklogViewModel])
async def get(id: str, request: Request):
    return await BacklogService.find_by_user(request.app.database, id)