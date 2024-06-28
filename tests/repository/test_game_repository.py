import os
import uuid
from dotenv import load_dotenv
from pymongo import MongoClient
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.game import GameModel, GameUpdateModel
from repositories.game_repository import GameRepository

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
async def game_mock():
    return GameModel(
        _id=str(uuid.uuid4()),
        title='Game Test',
        description='Description Test',
        platforms=['3fa85f64-5717-4562-b3fc-2c963f66afa6'],
        genres=['3fa85f64-5717-4562-b3fc-2c963f66afa6'],
        release_date='2024-06-21T18:15:15.187+00:00',
        developer='developer',
        publisher='publisher'
    )

@pytest_asyncio.fixture
async def game_updated_mock():
    return GameUpdateModel(
        _id=str(uuid.uuid4()),
        title='Game Test Updated',
        description='Description Test Updated',
        platforms=['3fa85f64-5717-4562-b3fc-2c963f66afa6'],
        genres=['3fa85f64-5717-4562-b3fc-2c963f66afa6'],
        release_date='2024-06-21T18:15:15.187+00:00',
        developer='developer updated',
        publisher='publisher updated'
    )

@pytest.mark.asyncio
async def test_create_game(db, game_mock):
    game_repository = GameRepository()
    game = await game_repository.create(db, game_mock)
    assert game is not None

@pytest.mark.asyncio
async def test_update_game(db, game_mock, game_updated_mock):
    await GameRepository.create(db, game_mock)
    updated_game = await GameRepository.update(db, game_mock.id, game_updated_mock)
    assert updated_game is not None

@pytest.mark.asyncio
async def test_delete_game(db, game_mock):
    await GameRepository.create(db, game_mock)
    result = await GameRepository.delete(db, game_mock.id)
    assert result is True

@pytest.mark.asyncio
async def test_find_all_games(db, game_mock):
    await GameRepository.create(db, game_mock)
    
    games = await GameRepository.find_all(db)
    
    game_list = [game for game in games]
    assert len(game_list) == 1
    
@pytest.mark.asyncio
async def test_find_game_by_id(db, game_mock):
    await GameRepository.create(db, game_mock)
    result = GameRepository.find_by_id(db, game_mock.id)
    result_data = result
    assert result_data is not None

@pytest.mark.asyncio
async def test_title_exists(db, game_mock):
    await GameRepository.create(db, game_mock)
    result = GameRepository.title_exists(db, game_mock.title)
    result_data = result
    assert result_data is not None

@pytest.mark.asyncio
async def test_exists(db, game_mock):
    await GameRepository.create(db, game_mock)
    result = GameRepository.exists(db, game_mock.id)
    result_data = result
    assert result_data is not None