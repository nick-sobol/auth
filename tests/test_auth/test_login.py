import pytest

from tests.mock_for_tests import UserData
from tests.test_conf import LOGIN_URL


@pytest.mark.usefixtures('create_user')
class TestUserLogin:

    async def test_login_with_true_credentials(self, test_cli):

        response = await test_cli.post(LOGIN_URL, data=UserData.valid_data)
        assert response.status == 200

    async def test_login_with_nonexistent_user(self, test_cli):

        response = await test_cli.post(LOGIN_URL,
                                       data=UserData.nonexistent_user)
        assert response.status == 404

    async def test_login_with_invalid_username(self, test_cli):

        response = await test_cli.post(LOGIN_URL,
                                       data=UserData.invalid_username)
        assert response.status == 422

    async def test_login_with_blank_username(self, test_cli):

        response = await test_cli.post(LOGIN_URL,
                                       data=UserData.blank_username)
        assert response.status == 422

    async def test_login_with_blank_password(self, test_cli):

        response = await test_cli.post(LOGIN_URL,
                                       data=UserData.blank_passwords)
        assert response.status == 422