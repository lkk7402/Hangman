from django.shortcuts import render,HttpResponse,redirect
from .models import HangmanGame
import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
    max_incorrect_guesses = len(selected_word)/2
    
    # Create a new HangmanGame instance with initial state
    new_game = HangmanGame.objects.create(
        word_to_guess=selected_word,
        current_state='_' * len(selected_word),  # Initial state with underscores
        incorrect_guesses_made=0,  # No incorrect guesses made yet
        remaining_guesses=max_incorrect_guesses,
        game_status='InProgress'
    )
    # Return the ID of the newly created game object in the HTTP response
    return JsonResponse({'id': new_game.id})
    # Redirect to the games page after starting a new game
    #return redirect('games')
   # return render(request, 'new.html')
   
def game_state(request, id):
    # Retrieve the HangmanGame instance based on the provided ID
    game = get_object_or_404(HangmanGame, pk=id)

    # Prepare the game state data
    game_state = {
        'current_state': game.current_state,
        'word_state': ''.join([letter if letter in game.current_state else '_' for letter in game.word_to_guess]),
        'incorrect_guesses_made': game.incorrect_guesses_made,
        'remaining_guesses': game.remaining_guesses,
        'game_status': game.game_status
    }

    # Return the game state in the HTTP response
    return JsonResponse(game_state)  
def make_guess(request, id):
    # Retrieve the HangmanGame instance based on the provided ID
    game = get_object_or_404(HangmanGame, pk=id)

    # Get the guessed character from the request
    guess = request.GET.get('guess')

    # Check if the guessed character is in the word to guess
    if guess in game.word_to_guess:
        # Update the current state of the game with the correct guess
        game.current_state = ''.join([letter if letter == guess or letter in game.current_state else '_' for letter in game.word_to_guess])
        # Update game status if the current state matches the word to guess
        if game.current_state == game.word_to_guess:
            game.game_status = 'Won'
        guess_correct = True
    else:
        # Update the number of incorrect guesses made
        game.incorrect_guesses_made += 1
        # Update game status if the player has used all remaining guesses
        if game.incorrect_guesses_made >= game.remaining_guesses:
            game.game_status = 'Lost'
        guess_correct = False

    # Decrement the number of remaining guesses only if the guess is incorrect
    if not guess_correct:
        game.remaining_guesses -= 1

    # Save the updated game state
    game.save()

    # Prepare the game state data
    game_state = {
        'current_state': game.current_state,
        'word_state': ''.join([letter if letter in game.current_state else '_' for letter in game.word_to_guess]),
        'incorrect_guesses_made': game.incorrect_guesses_made,
        'remaining_guesses': game.remaining_guesses,
        'game_status': game.game_status,
        'guess_correct': guess_correct
    }

    # Return the updated game state in the HTTP response
    return JsonResponse(game_state)