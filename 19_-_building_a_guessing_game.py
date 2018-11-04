# Secret word is defined and user has 3 attempts to try to guess it in order to win.
secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# "while" loop checks if the user has guessed the word and that the user is not of guesses.
# "if" statement checks if the number of time the user has guessed is less than the limit.
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# Final "if" statement prints the result of the game.
if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")
