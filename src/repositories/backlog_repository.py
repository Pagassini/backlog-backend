

from models.backlog import BacklogModel, BacklogUpdateModel


class BacklogRepository:

    @staticmethod
    async def create(db, backlog: BacklogModel):
        backlog_dict = backlog.dict(by_alias=True)
        backlog_dict["_id"] = str(backlog_dict["_id"])
        result = db['backlogs'].insert_one(backlog_dict)
        backlog_dict['_id'] = str(result.inserted_id)
        return backlog_dict
    
    @staticmethod
    async def update(db, id: str, backlog: BacklogUpdateModel):
        update_data = {k: v for k, v in backlog.dict(exclude_unset=True).items()}
        db["backlogs"].update_one({"_id": id}, {"$set": update_data})
        updated_backlog = db["backlogs"].find_one({"_id": id})
        updated_backlog["_id"] = str(updated_backlog["_id"])
        return updated_backlog
    
    @staticmethod
    async def delete(db, id: str):
        result = db['backlogs'].delete_one({"_id": id})
        return result.deleted_count > 0
    
    @staticmethod
    async def find_by_user(db, id: str):
        return db['backlogs'].find({"user_id": id})
    
    @staticmethod
    async def exists(db, id: str):
        return db['backlogs'].find_one({"_id": id})
    
    @staticmethod
    async def game_exists_in_user_backlog(db, user_id: str, game_id: str):
        return db['backlogs'].find_one({"user_id": user_id, "game_id": game_id})