from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game, name='games'),
    path('game/new', views.new_game, name='new_game'),
    path('game/<int:id>/', views.game_state, name='game_state'),  # New URL pattern for game state endpoint
]