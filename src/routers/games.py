from typing import List
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models.game import GameModel, GameUpdateModel


router = APIRouter()

@router.post("/", response_description='Post a Game', status_code=status.HTTP_201_CREATED, response_model=GameModel)
def post_game(request: Request, game: GameModel = Body(...)):
    game = jsonable_encoder(game)
    new_game = request.app.database["games"].insert_one(game)
    created_game = request.app.database["games"].find_one({
        "_id": new_game.inserted_id
    })
    
    return created_game

@router.get("/", response_description='Get all Games', response_model=List[GameModel])
def get_games(request: Request):
    games = list(request.app.database["games"].find(limit=50))

    return games

@router.delete("/", response_description='Delete a Game')
def delete_game(id: str, request: Request, response: Response):
    request.app.database["games"].delete_one({"_id": id})

@router.put("/", response_description='Update a Game', response_model=GameModel)
def update_game(id: str, request: Request, game: GameUpdateModel = Body(...)):
    update_data = {k: v for k, v in game.dict(exclude_unset=True).items()}
    
    request.app.database["games"].update_one({"_id": id}, {"$set": update_data})
    
    updated_game = request.app.database["games"].find_one({"_id": id})
    
    return updated_game
