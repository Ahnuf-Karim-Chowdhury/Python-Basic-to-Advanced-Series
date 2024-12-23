import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●  ●  ● │",
        "│ ●  ●  ● │",
        "│ ●  ●  ● │",
        "└─────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How Many Dice? : "))

# Rolling the dice
for _ in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Printing the dice faces
for line in range(5):  # 5 lines for each dice art
    for die in dice:
        print(dice_art[die][line], end=" ")
    print()  # Move to the next line

# Calculating and printing the total
total = sum(dice)
print(f"Total: {total}")
