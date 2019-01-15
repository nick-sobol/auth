import pytest

from tests.mock_for_tests import UserData
from tests.test_conf import REGISTRATION_URL


@pytest.mark.usefixtures('clear_db_tables')
class TestUserRegistration:

    async def test_registration_with_valid_user(self, test_cli):

        response = await test_cli.post(REGISTRATION_URL,
                                       data=UserData.valid_data)
        assert response.status == 200

    async def test_registration_with_blank_username(self, test_cli):

        response = await test_cli.post(REGISTRATION_URL,
                                       data=UserData.blank_username)
        assert response.status == 422

    async def test_registration_with_too_long_passwords(self, test_cli):

        response = await test_cli.post(REGISTRATION_URL,
                                       data=UserData.invalid_passwords_length)
        assert response.status == 422

    async def test_registration_with_no_password_match(self, test_cli):

        response = await test_cli.post(REGISTRATION_URL,
                                       data=UserData.no_passwords_match)
        assert response.status == 422

    async def test_registration_with_no_username(self, test_cli):

        response = await test_cli.post(REGISTRATION_URL,
                                       data=UserData.blank_username)
        assert response.status == 422

    async def test_registration_with_no_passwords(self, test_cli):

        response = await test_cli.post(REGISTRATION_URL,
                                       data=UserData.blank_passwords)
        assert response.status == 422