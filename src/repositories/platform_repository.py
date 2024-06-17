

from models.platform import PlatformModel


class PlatformRepository:
    
    @staticmethod
    async def find_all(db):
        platforms = db["platforms"].find()
        return platforms
    
    @staticmethod
    async def exists(db, id: str) -> bool:
        return db["platforms"].find_one({"_id": id})
    
    @staticmethod
    async def create(db, platform: PlatformModel):
        platform_dict = platform.dict(by_alias=True)
        platform_dict["_id"] = str(platform_dict["_id"])
        result = db['platforms'].insert_one(platform_dict)
        platform_dict['_id'] = str(result.inserted_id)
        return platform_dict