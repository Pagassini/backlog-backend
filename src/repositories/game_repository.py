from models.game import GameModel, GameUpdateModel


class GameRepository:
    
    @staticmethod
    async def create(db, game: GameModel):
        game_dict = game.model_dump(by_alias=True)
        game_dict["_id"] = str(game_dict["_id"])
        result = await db['games'].insert_one(game_dict)
        game_dict['_id'] = str(result.inserted_id)
        return game_dict
    
    @staticmethod
    async def update(db, id: str, game: GameUpdateModel):
        update_data = {k: v for k, v in game.model_dump(exclude_unset=True).items()}
        await db["games"].update_one({"_id": id}, {"$set": update_data})
        updated_game = await db["games"].find_one({"_id": id})
        updated_game["_id"] = str(updated_game["_id"])
        return updated_game
    
    @staticmethod
    async def delete(db, id: str):
        result = await db['games'].delete_one({"_id": id})
        return result.deleted_count > 0
    
    @staticmethod
    async def find_all(db):
        return db['games'].find()
    
    @staticmethod
    async def find_by_id(db, id: str):
        return db['games'].find_one(id)
    
    @staticmethod
    async def title_exists(db, title: str):
        return db['games'].find_one({"title": title})
    
    @staticmethod
    async def exists(db, id: str):
        return db['games'].find_one({"_id": id})
        