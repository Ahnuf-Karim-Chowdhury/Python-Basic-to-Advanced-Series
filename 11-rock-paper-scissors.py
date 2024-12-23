import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose 'rock', 'paper', or 'scissors'.")

    # Get player choice
    player_choice = input("Enter your choice: ").strip().lower()
    
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return

    # Get computer choice
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    # Determine and print the result
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Start the game
rock_paper_scissors()
