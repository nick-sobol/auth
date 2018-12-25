from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import text

from config import JINJA as jinja


bp = Blueprint('auth')


class AuthView(HTTPMethodView):

    async def get(self, request):
        return jinja.render('auth/register.html', request)


class RegisterView(AuthView):

    async def post(self, request):
        userdata = {
            'name': request.form.get('username'),
            'password': request.form.get('password'),
            'confirm_password': request.form.get('confirm-password'),
        }

        return text('request succeed')


class LoginView(AuthView):

    async def post(self, request):
        return text(request.form)


bp.add_route(RegisterView.as_view(), '/register', name='Register')
bp.add_route(LoginView.as_view(), '/login', name='Login')

















