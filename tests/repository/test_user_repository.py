from dotenv import load_dotenv
import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.genre import GenreModel
from models.user import UserModel, UserUpdateModel
from repositories.genre_repository import GenreRepository
from repositories.user_repository import UserRepository

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
async def user_mock():
    return UserModel(
        _id=str(uuid.uuid4()),
        email='test@test.com',
        password='test',
        username='test'
    )

@pytest_asyncio.fixture
async def user_updated_mock():
    return UserUpdateModel(
        email='test@test.com',
        password='test',
        username='test'
    )
    
@pytest.mark.asyncio
async def test_create_user(db, user_mock):
    user_repository = UserRepository()
    user = await user_repository.create(db, user_mock)
    assert user is not None

@pytest.mark.asyncio
async def test_update_user(db, user_mock, user_updated_mock):
    await UserRepository.create(db, user_mock)
    updated_user = await UserRepository.update(db, user_mock.id, user_updated_mock)
    assert updated_user is not None

@pytest.mark.asyncio
async def test_delete_user(db, user_mock):
    await UserRepository.create(db, user_mock)
    result = await UserRepository.delete(db, user_mock.id)
    assert result is True

@pytest.mark.asyncio
async def test_find_all_users(db, user_mock):
    await UserRepository.create(db, user_mock)

    users = await UserRepository.find_all(db)

    user_list = [user async for user in users]
    assert len(user_list) == 1

@pytest.mark.asyncio
async def test_username_exists(db, user_mock):
    await UserRepository.create(db, user_mock)
    result = await UserRepository.username_exists(db, user_mock.username)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_email_exists(db, user_mock):
    await UserRepository.create(db, user_mock)
    result = await UserRepository.email_exists(db, user_mock.email)
    result_data = await result
    assert result_data is not None

@pytest.mark.asyncio
async def test_exists(db, user_mock):
    await UserRepository.create(db, user_mock)
    result = await UserRepository.exists(db, user_mock.id)
    result_data = await result
    assert result_data is not None