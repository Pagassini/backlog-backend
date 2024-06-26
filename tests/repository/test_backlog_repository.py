from dotenv import load_dotenv
import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.backlog import BacklogModel, BacklogUpdateModel
from repositories.backlog_repository import BacklogRepository

load_dotenv()

@pytest_asyncio.fixture
async def db():
    db_uri = os.getenv('MONGODB_CONNECTION_URI')
    if not db_uri:
        raise ValueError("Connection string could not be found")
    
    client = AsyncIOMotorClient(db_uri)
    db = client['test_database']
    
    await client.drop_database('test_database')
    
    yield db
    
    await client.drop_database('test_database')
    client.close()
    
@pytest_asyncio.fixture
async def backlog_mock():
    return BacklogModel(
        _id=str(uuid.uuid4()),
        game_id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
        user_id='3fa85f64-5717-4562-b3fc-2c963f66afa6',
        status='playing'
    )
    
@pytest_asyncio.fixture
async def backlog_updated_mock():
    return BacklogUpdateModel(
        status='finished'
    )

@pytest.mark.asyncio
async def test_create_backlog(db, backlog_mock):
    backlog_repository = BacklogRepository()
    backlog = await backlog_repository.create(db, backlog_mock)
    assert backlog is not None

@pytest.mark.asyncio
async def test_update_backlog(db, backlog_mock, backlog_updated_mock):
    await BacklogRepository.create(db, backlog_mock)
    updated_backlog = await BacklogRepository.update(db, backlog_mock.id, backlog_updated_mock)
    assert updated_backlog is not None

@pytest.mark.asyncio
async def test_delete_backlog(db, backlog_mock):
    await BacklogRepository.create(db, backlog_mock)
    result = await BacklogRepository.delete(db, backlog_mock.id)
    assert result is True
    
@pytest.mark.asyncio
async def test_find_backlog_by_user(db, backlog_mock):
    await BacklogRepository.create(db, backlog_mock)
    result = BacklogRepository.find_by_user(db, backlog_mock.id)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_exists(db, backlog_mock):
    await BacklogRepository.create(db, backlog_mock)
    result = BacklogRepository.exists(db, backlog_mock.id)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_game_exists_in_user_backlog(db, backlog_mock):
    await BacklogRepository.create(db, backlog_mock)
    result = BacklogRepository.game_exists_in_user_backlog(db, backlog_mock.id, backlog_mock.game_id)
    result_data = await result
    assert result_data is not None