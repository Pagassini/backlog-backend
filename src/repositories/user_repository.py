

from models.user import UserModel, UserUpdateModel


class UserRepository:
    
    @staticmethod
    async def create(db, user: UserModel):
        user_dict = user.dict(by_alias=True)
        user_dict["_id"] = str(user_dict["_id"])
        result = db['users'].insert_one(user_dict)
        user_dict["_id"] = str(result.inserted_id)
        return user_dict
    
    @staticmethod
    async def update(db, id: str, user: UserUpdateModel):
        update_data = {k: v for k, v in user.dict(exclude_unset=True).items()}
        db["users"].update_one({"_id": id}, {"$set": update_data})
        updated_user = db["users"].find_one({"_id": id})
        updated_user["_id"] = str(updated_user["_id"])
        return updated_user
    
    @staticmethod
    async def delete(db, id: str):
        result = db['users'].delete_one({"_id": id})
        return result.deleted_count > 0
    
    @staticmethod
    async def find_all(db):
        return db['users'].find()
    
    @staticmethod
    async def username_exists(db, username: str):
        return db['users'].find_one({"username": username})
    
    @staticmethod
    async def email_exists(db, email: str):
        return db['users'].find_one({"email": email})
    
    @staticmethod
    async def exists(db, id: str):
        return db['users'].find_one({"_id": id})
    
