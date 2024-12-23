import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Set the range for the random number
    low = 1
    high = 100
    number_to_guess = random.randint(low, high)
    
    attempts = 0
    guess = None
    
    while guess != number_to_guess:
        try:
            guess = int(input(f"Guess a number between {low} and {high}: "))
            
            if guess < low or guess > high:
                print(f"Please enter a number between {low} and {high}.")
                continue
            
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# Start the game
number_guessing_game()
