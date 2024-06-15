import os
from bson import UuidRepresentation
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import dotenv_values
from api.routers.games import router as game_router

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
config = dotenv_values(dotenv_path)

app = FastAPI()

app.include_router(game_router, tags=["games"], prefix="/games")

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"], uuidRepresentation='standard')
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
