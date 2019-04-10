from django.shortcuts import render
from django.http import HttpRequest
from .models import Game

# Create your views here.
def index(request: HttpRequest):
  return render(request, "regency_app/index.html", context={})


def join_game(request: HttpRequest):
  games = Game.objects.order_by("-start_date")[:5]
  return render(request, "regency_app/join_game.html", context={"games_list": games})