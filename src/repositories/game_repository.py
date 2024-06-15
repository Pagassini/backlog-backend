


from bson import ObjectId
from fastapi import HTTPException
from models.game import GameModel, GameUpdateModel


class GameRepository:
    
    @staticmethod
    async def create(db, game: GameModel):
        game_dict = game.dict(by_alias=True)
        result = db['games'].insert_one(game_dict)
        game_dict['_id'] = str(result.inserted_id)
        return game_dict
    
    @staticmethod
    async def update(db, id: str, game: GameUpdateModel):
        update_data = {k: v for k, v in game.dict(exclude_unset=True).items()}
        result = db["games"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 0:
            raise HTTPException(status_code=404)
        updated_game = db["games"].find_one({"_id": ObjectId(id)})
        updated_game["_id"] = str(updated_game["_id"])
        return updated_game
    
    @staticmethod
    async def delete(db, id: str):
        result = db['games'].delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
    
    @staticmethod
    async def find_all(db):
        games = db['games'].find(limit=50)
        return games