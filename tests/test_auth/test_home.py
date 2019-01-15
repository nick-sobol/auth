import pytest

from tests.test_conf import HOME_URL, LOGOUT_URL


class TestHomePageAccessibility:

    async def test_guest_access(self, test_cli):
        response = await test_cli.get(HOME_URL)

        assert response.status == 401

    @pytest.mark.usefixtures('login_user')
    async def test_valid_user_access(self, test_cli):

        response = await test_cli.get(HOME_URL)

        assert response.status == 200

    @pytest.mark.usefixtures('login_user')
    async def test_logout_from_home(self, test_cli):

        response = await test_cli.post(LOGOUT_URL)
        assert response.status == 204

        response = await test_cli.get(HOME_URL)
        assert response.status == 401