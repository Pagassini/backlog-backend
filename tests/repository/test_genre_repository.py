from dotenv import load_dotenv
import os
import uuid
from dotenv import load_dotenv
from pymongo import MongoClient
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.genre import GenreModel
from repositories.genre_repository import GenreRepository

load_dotenv()

@pytest_asyncio.fixture
async def db():
    db_uri = os.getenv('MONGODB_CONNECTION_URI')
    if not db_uri:
        raise ValueError("Connection string could not be found")
    
    client = MongoClient(db_uri)
    db = client['test_database']
    
    client.drop_database('test_database')
    
    yield db
    
    client.drop_database('test_database')
    client.close()
    
@pytest_asyncio.fixture
async def genre_mock():
    return GenreModel(
        _id=str(uuid.uuid4()),
        name='test'
    )
    
@pytest.mark.asyncio
async def test_create_genre(db, genre_mock):
    genre_repository = GenreRepository()
    genre = genre_repository.create(db, genre_mock)
    assert genre is not None
    
@pytest.mark.asyncio
async def test_find_all_genres(db, genre_mock):
    await GenreRepository.create(db, genre_mock)

    genres = await GenreRepository.find_all(db)

    genre_list = [genre for genre in genres]
    assert len(genre_list) == 1

@pytest.mark.asyncio
async def test_name_exists(db, genre_mock):
    await GenreRepository.create(db, genre_mock)
    result = GenreRepository.name_exists(db, genre_mock.name)
    result_data = result
    assert result_data is not None