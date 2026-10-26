from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from categories.models import Category
from games.forms import BoardGameCreateForm, BoardGameDeleteForm, BoardGameEditForm
from games.models import BoardGame

def index(request: HttpRequest) -> HttpResponse:
    category_id = request.GET.get('category')
    games = BoardGame.objects.all()

    if category_id:
        games = games.filter(categories=category_id)

    categories = Category.objects.all()

    context = {
        'games': games,
        'categories': categories,
        'category_id': category_id,
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
        form = BoardGameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_details', pk=pk)
    else:
        form = BoardGameEditForm(instance=game)

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