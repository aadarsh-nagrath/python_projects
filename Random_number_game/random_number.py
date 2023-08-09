import random

def play_game():
    random_number = random.randint(0, 10)
    turns = 3
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 10. Can you guess it?")
    
    while turns > 0:
        guess = int(input("Enter your guess: "))
        
        if guess == random_number:
            print(f"Congratulations! You guessed the correct number! It was {random_number}.")
            break
        
        turns -= 1
    
    if turns == 0:
        print(f"Sorry, you're out of turns! The number was {random_number}. Better luck next time!")

def main():
    while True:
        play_game()
        play_again = input("Press any key to play again, or 'q' to quit: ")
        if play_again.lower() == 'q':
            break

if __name__ == "__main__":
    main()
