from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game, name='games'),
    path('new/', views.new_game, name='new_game'),

]