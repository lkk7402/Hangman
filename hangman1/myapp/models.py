from django.db import models

class HangmanGame(models.Model):
    word_to_guess = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
    incorrect_guesses_made = models.PositiveIntegerField(default=0)
    remaining_guesses = models.PositiveIntegerField(default=6)
    game_status = models.CharField(max_length=10, default='InProgress')