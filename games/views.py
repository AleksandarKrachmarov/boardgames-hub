from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from games.forms import BoardGameCreateForm, BoardGameDeleteForm
from games.models import BoardGame

def index(request: HttpRequest) -> HttpResponse:
    games = BoardGame.objects.all()
    context = {
        'games': games,
    }

    return render(request, 'games/index.html', context)

def create_game(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = BoardGameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BoardGameCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'games/create_game.html', context)

def game_details(request: HttpRequest, pk: int) -> HttpResponse:
    game = get_object_or_404(BoardGame, pk=pk)
    context = {
        'game': game,
    }
    return render(request, 'games/game_details.html', context)

def edit_game(request: HttpRequest, pk: int) -> HttpResponse:
    game = get_object_or_404(BoardGame, pk=pk)
    if request.method == 'POST':
        form = BoardGameCreateForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_details', pk=pk)
    else:
        form = BoardGameCreateForm(instance=game)

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'games/edit_game.html', context)

def delete_game(request: HttpRequest, pk: int) -> HttpResponse:
    game = get_object_or_404(BoardGame, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('index')

    form = BoardGameDeleteForm(instance=game)

    context = {
        'game': game,
        'form': form
    }

    return render(request, 'games/delete_game.html', context)