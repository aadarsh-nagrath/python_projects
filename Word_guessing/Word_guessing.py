import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_ "
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6 

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct!")
        else:
            attempts_left -= 1
            print("Incorrect. Attempts left:", attempts_left)

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("\nCongratulations! You guessed the word correctly:", word_to_guess)
            break

    if attempts_left == 0:
        print("\nGame over. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
