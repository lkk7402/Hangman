from django.shortcuts import render,HttpResponse
from .models import HangmanGame

# Create your views here.
def home(request):
    return render(request, 'home.html')
def game(request):
    item = HangmanGame.objects.all()
    return render(request, 'games.html', {'games': item})
