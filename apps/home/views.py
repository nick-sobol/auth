from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic_jwt.decorators import protected

from config import JINJA as jinja

bp = Blueprint('home')


class HomeView(HTTPMethodView):
    decorators = [protected()]

    async def get(self, request):

        return jinja.render('home.html', request)


bp.add_route(HomeView.as_view(), '/home', name='home')