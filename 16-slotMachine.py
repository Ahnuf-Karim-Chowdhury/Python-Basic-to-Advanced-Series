import random
import time

def spin_slot_machine():
    # Define emojis for the slot machine
    emojis = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍎", "🍓", "🍑"]
    return [random.choice(emojis) for _ in range(3)]

def display_result(result):
    print(" | ".join(result))
    print()

def main():
    print("Welcome to the Slot Machine!")
    time.sleep(1)  # Short delay for effect

    while True:
        input("Press Enter to spin the slot machine...")

        result = spin_slot_machine()
        display_result(result)
        
        if result[0] == result[1] == result[2]:
            print("Congratulations! You won!")
        else:
            print("Try again!")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            break

    print("Thanks for playing! Goodbye!")

main()
