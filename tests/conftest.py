import pytest
from main import create_app
from database import get_engine

from apps.auth.models import User
from tests.mock_for_tests import UserData


@pytest.yield_fixture
def app():
    app = create_app()
    yield app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))


@pytest.fixture
async def clear_db_tables(request):
    yield
    engine = await get_engine()

    async with engine.acquire() as conn:
        await conn.execute(User.delete())


@pytest.fixture
async def create_user(test_cli, clear_db_tables):
    await test_cli.post('/auth/register', data=UserData.valid_data)


@pytest.fixture
async def login_user(test_cli, create_user):
    return await test_cli.post('/auth/login', data=UserData.valid_data)