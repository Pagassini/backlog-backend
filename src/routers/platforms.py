


from typing import List
from fastapi import APIRouter, Request

from models.dtos.platform_dto import PlatformCreateDTO
from models.viewmodels.platform_viewmodel import PlatformViewModel
from services.platform_service import PlatformService


router = APIRouter()

@router.post("", response_model=PlatformViewModel)
async def post(platform: PlatformCreateDTO, request: Request):
    return await PlatformService.create(request.app.database, platform)

@router.get("", response_model=List[PlatformViewModel])
async def get(request: Request):
    return await PlatformService.find_all(request.app.database)