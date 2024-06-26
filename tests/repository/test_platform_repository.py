from dotenv import load_dotenv
import os
import uuid
from dotenv import load_dotenv
import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from models.genre import GenreModel
from models.platform import PlatformModel
from repositories.genre_repository import GenreRepository
from repositories.platform_repository import PlatformRepository

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
async def platform_mock():
    return PlatformModel(
        _id=str(uuid.uuid4()),
        name='test'
    )
    
@pytest.mark.asyncio
async def test_create_platform(db, platform_mock):
    platform_repository = PlatformRepository()
    platform = await platform_repository.create(db, platform_mock)
    assert platform is not None
    
@pytest.mark.asyncio
async def test_find_all_platforms(db, platform_mock):
    await PlatformRepository.create(db, platform_mock)

    platforms = PlatformRepository.find_all(db)

    platform_list = [platform async for platform in await platforms]
    assert len(platform_list) == 1
    
@pytest.mark.asyncio
async def test_exists(db, platform_mock):
    await PlatformRepository.create(db, platform_mock)
    result = PlatformRepository.exists(db, platform_mock.id)
    result_data = await result
    assert result_data is not None
    
@pytest.mark.asyncio
async def test_name_exists(db, platform_mock):
    await PlatformRepository.create(db, platform_mock)
    result = PlatformRepository.name_exists(db, platform_mock.name)
    result_data = await result
    assert result_data is not None