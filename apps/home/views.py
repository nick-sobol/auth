from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic_jwt.decorators import protected
from sanic.response import text

bp = Blueprint('home')


class HomeView(HTTPMethodView):
    decorators = [protected()]

    async def get(self, request):
        return text('Protected text received')


bp.add_route(HomeView.as_view(), '/home', name='home')