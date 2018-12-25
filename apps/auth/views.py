from sanic_jwt import BaseEndpoint

from config import JINJA as jinja


class Register(BaseEndpoint):

    async def get(self, request):
        return jinja.render('auth/register.html', request)

    async def post(self, request, *args, **kwargs):

        user = await request.app.auth.authenticate(request, *args, **kwargs)

        access_token, output = await self.responses.get_access_token_output(
            request,
            user,
            self.config,
            self.instance
        )

        response = self.responses.get_token_reponse(
            request,
            access_token,
            output,
            config=self.config
        )

        return response


my_views = (
    ('/register', Register),
)