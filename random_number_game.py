import random

# Number Guessing Game

# Create a random number between 1 and 100
random_number = random.randint(1, 100)

# Game loop
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")

    while True:
        try:
# Accept user guess
            guess = int(input("Enter your guess: "))
            
            if guess < random_number:
                print("Too low! Try again.")   
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number: {random_number}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
number_guessing_game()
