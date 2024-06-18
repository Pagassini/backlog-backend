from typing import List
from models.dtos.platform_dto import PlatformCreateDTO
from models.platform import PlatformModel
from models.viewmodels.platform_viewmodel import PlatformViewModel
from repositories.platform_repository import PlatformRepository


class PlatformService:
    
    @staticmethod
    async def create(db, platform_dto: PlatformCreateDTO) -> PlatformViewModel:
        
        platform_model = PlatformModel(
            name=platform_dto.name
        )
        
        created_platform = await PlatformRepository.create(db, platform_model)
        return PlatformViewModel(**created_platform)
    
    @staticmethod
    async def find_all(db) -> List[PlatformViewModel]:
        platforms_cursor = await PlatformRepository.find_all(db)
        platforms = []
        for platform in platforms_cursor:
            platform_view_model = PlatformViewModel(**platform)
            platforms.append(platform_view_model)
        return platforms