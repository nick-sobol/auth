from sanic_jwt import BaseEndpoint
from sanic.response import HTTPResponse
from sanic_jwt.decorators import protected
from sanic.response import redirect
from config import JINJA as jinja


class RegisterView(BaseEndpoint):

    async def get(self, request):
        return jinja.render('auth/register.html', request)

    async def post(self, request, *args, **kwargs):
        request.form['register_enabled'] = [True]

        await request.app.auth.authenticate(request, *args, **kwargs)

        return redirect('/auth/login')


class LoginView(BaseEndpoint):

    async def get(self, request):
        return jinja.render('auth/login.html', request)

    async def post(self, request, *args, **kwargs):

        user = await request.app.auth.authenticate(request, *args, **kwargs)

        access_token, _ = await self.responses.get_access_token_output(
            request,
            user,
            self.config,
            self.instance
        )

        response = HTTPResponse()

        response.cookies['access_token'] = access_token

        return redirect('/home', headers=response.headers)


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
