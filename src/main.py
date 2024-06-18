import os
from fastapi import FastAPI, status
from pymongo import MongoClient
from dotenv import dotenv_values
from exceptions.game_exceptions import GameNotFoundException
from exceptions.genre_exceptions import GenreNotFoundException
from exceptions.handlers.game_exception_handler import GameExceptionHandler
from exceptions.handlers.genre_exception_handler import GenreExceptionHandler
from exceptions.handlers.platform_exception_handler import PlatformExceptionHandler
from exceptions.platform_exceptions import PlatformNotFoundException
from routers.games import router as game_router
from routers.genre import router as genre_router
from routers.platforms import router as platform_router

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
config = dotenv_values(dotenv_path)

app = FastAPI(title=config['PROJECT_NAME'])

app.include_router(game_router, tags=["Games"], prefix=f"{config['PREFIX']}/games")
app.include_router(genre_router, tags=["Genres"], prefix=f"{config['PREFIX']}/genres")
app.include_router(platform_router, tags=["Platforms"], prefix=f"{config['PREFIX']}/platforms")

app.add_exception_handler(
    exc_class_or_status_code=GameNotFoundException,
    handler=GameExceptionHandler.create_exception_handler(
        status.HTTP_404_NOT_FOUND
    ),
)

app.add_exception_handler(
    exc_class_or_status_code=PlatformNotFoundException,
    handler=PlatformExceptionHandler.create_exception_handler(
        status.HTTP_404_NOT_FOUND
    )
)

app.add_exception_handler(
    exc_class_or_status_code=GenreNotFoundException,
    handler=GenreExceptionHandler.create_exception_handler(
        status.HTTP_404_NOT_FOUND
    )
)

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
