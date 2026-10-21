from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

from games.models import BoardGame

def index(request: HttpRequest) -> HttpResponse:
    games = BoardGame.objects.all()
    context = {
        'games': games,
    }

    return render(request, 'games/index.html', context)