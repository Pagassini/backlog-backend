import os
from bson import UuidRepresentation
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from routers.games import router as game_router
from routers.genre import router as genre_router
from routers.platforms import router as platform_router

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
config = dotenv_values(dotenv_path)

app = FastAPI()

app.include_router(game_router, tags=["Games"], prefix="/api/v1/games")
app.include_router(genre_router, tags=["Genres"], prefix="/api/v1/genres")
app.include_router(platform_router, tags=["Platforms"], prefix="/api/v1/platforms")

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
