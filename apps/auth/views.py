from sanic_jwt import BaseEndpoint
from sanic.response import HTTPResponse
from sanic_jwt.decorators import protected

from config import JINJA as jinja


class AuthView(BaseEndpoint):

    async def post(self, request, *args, **kwargs):

        user = (
            await request.app.auth.authenticate(request, *args, **kwargs)
        )

        access_token, output = await self.responses.get_access_token_output(
            request,
            user,
            self.config,
            self.instance
        )

        self.responses.get_token_reponse(
            request,
            access_token,
            output,
            config=self.config
        )

        response = HTTPResponse(status=200)

        response.cookies['access_token'] = access_token

        return response


class RegisterView(AuthView):

    async def get(self, request):
        return jinja.render('auth/register.html', request)


class LoginView(AuthView):

    async def get(self, request):
        return jinja.render('auth/login.html', request)


class LogoutView(BaseEndpoint):
    decorators = [protected()]

    async def delete(self, request):
        response = HTTPResponse(204)
        del response.cookies['access_token']

        return response



jwt_views = (
    ('/register', RegisterView),
    ('/login', LoginView),
    ('/logout', LogoutView),
)
