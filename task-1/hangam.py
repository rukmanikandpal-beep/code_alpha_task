print("Welcome to Hangman Game!")

import random

words = [
    "python","java","javascript","html","css","react","angular","nodejs","django","flask"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
while wrong_guesses < max_wrong_guesses:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter")
        continue
    guessed_letters.append(guess)
    if guess not in word:
        wrong_guesses += 1
        print(
            f"Wrong guess! You have "
            f"{max_wrong_guesses - wrong_guesses} attempts left"
        )
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Game Over! The word was:", word)