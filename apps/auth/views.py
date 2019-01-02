from sanic.cookies import Cookie
from sanic.response import HTTPResponse, redirect
from sanic_jwt import BaseEndpoint
from sanic_jwt.decorators import protected

from config import JINJA as jinja

from .backend import authenticate


class RegisterView(BaseEndpoint):

    def get(self, request):
        return jinja.render('auth/register.html', request)

    async def post(self, request, *args, **kwargs):
        request.form['register_enabled'] = [True]

        await authenticate(request, *args, **kwargs)

        return redirect('/auth/login')


class LoginView(BaseEndpoint):

    def get(self, request):
        return jinja.render('auth/login.html', request)

    async def post(self, request, *args, **kwargs):

        user = await authenticate(request, *args, **kwargs)

        access_token, _ = await self.responses.get_access_token_output(
            request,
            user,
            self.config,
            self.instance
        )

        cookie = Cookie('access_token', access_token)
        cookie['path'] = '/'
        headers = {
            'Set-Cookie': cookie,
        }

        return redirect('/home', headers=headers)


class LogoutView(BaseEndpoint):
    decorators = [protected()]

    def post(self, request):
        response = HTTPResponse(status=204)
        del response.cookies['access_token']

        return response


jwt_views = (
    ('/register', RegisterView),
    ('/login', LoginView),
    ('/logout', LogoutView),
)
