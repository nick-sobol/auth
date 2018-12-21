from sanic import Blueprint, response
from sanic.views import HTTPMethodView
from settings import settings

jinja = settings.jinja
bp = Blueprint(__name__)


class AuthView(HTTPMethodView):

    async def get(self, request):
        return jinja.render('auth.html', request, name='Test name')


bp.add_route(AuthView.as_view(), '/auth')