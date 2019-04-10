from django.urls import path
from . import views

app_name = "regency_app"
urlpatterns = [
  path("", views.index, name="index"),
  path("games/", views.join_game, name="games"),
]