import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(attempts):
    stages = [
        '''
         ------
         |    |
         |    
         |   
         |    
         |    
         |    
        ------
        ''',
        '''
         ------
         |    |
         |    O
         |    
         |    
         |    
         |    
        ------
        ''',
        '''
         ------
         |    |
         |    O
         |    |
         |    
         |    
         |    
        ------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|
         |    
         |    
         |    
        ------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |    
         |    
         |    
        ------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |    
         |    
        ------
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |    
         |    
        ------
        '''
    ]
    return stages[6 - attempts]

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print(display_hangman(attempts))
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print(display_hangman(attempts))
        print("\nGame Over! The word was:", word)

hangman()
