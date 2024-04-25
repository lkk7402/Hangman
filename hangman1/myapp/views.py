from django.shortcuts import render,HttpResponse,redirect
from .models import HangmanGame
import random
# Create your views here.
def home(request):
    return render(request, 'home.html')
def game(request):
    item = HangmanGame.objects.all()
    return render(request, 'games.html', {'games': item})
def new_game(request):
    # List of words to choose from
    word_list = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]
    
    # Choose a random word from the list
    selected_word = random.choice(word_list)
    
    # Calculate the maximum incorrect guesses allowed
    max_incorrect_guesses = len(selected_word)
    
    # Create a new HangmanGame instance with initial state
    new_game = HangmanGame.objects.create(
        word_to_guess=selected_word,
        current_state='_' * len(selected_word),  # Initial state with underscores
        incorrect_guesses_made=0,  # No incorrect guesses made yet
        remaining_guesses=max_incorrect_guesses,
        game_status='InProgress'
    )
    
    # Redirect to the games page after starting a new game
    return redirect('games')
   # return render(request, 'new.html')

