# Python-Basic-to-Advanced-Series

This repository contains a collection for Beginner to Advanced Python programs designed to practice and demonstrate core programming concepts. Each program serves a unique purpose, ranging from utility tools to fun games.

---

## Table of Contents

**Basic Programs**

1. [Calculator Program](#1-calculator-program)
2. [Weight Converter Program](#2-weight-converter-program)
3. [Temperature Converter Program](#3-temperature-converter-program)
4. [Email Slicer Program](#4-email-slicer-program)
5. [Compound Interest Calculator Program](#5-compound-interest-calculator-program)
6. [Countdown Timer Program](#6-countdown-timer-program)
7. [Shopping Cart Program](#7-shopping-cart-program)

**Games**

8. [Quiz Game](#8-quiz-game)
9. [Concession Stand Program](#9-concession-stand-program)
10. [Number Guessing Game](#10-number-guessing-game)
11. [Rock-Paper-Scissors Game](rock-paper-scissors-game.md)  **New Entry**
12. [Dice Roller Program](dice-roller-program.md)  **New Entry**

**Advanced Programs**

13. [Encryption and Decryption Program](encryption-and- decryption-program.md)  **New Entry**
14. [Credit Card Validation Program](credit-card-validation-program.md)  **New Entry**
15. [Banking Program](banking-program.md)
    * [15.1 Upgraded Banking Program](upgraded-banking-program.md)  **New Entry**
16. [Slot Machine Program](slot-machine-program.md)  **New Entry**
17. [Hangman Game](hangman-game.md)  **New Entry**

**Graphical User Interface (GUI) Programs**

18. [Digital Clock Program using PyQt5](digital-clock-program-using-pyqt5.md)  **New Entry**
19. [Stop Watch Program PyQt5](stop-watch-program-pyqt5.md)  **New Entry**

**Web Applications**

20. [Weather App](weather-app.md)  **New Entry**

**Security**

21. [Password Manager using AES-256 & RSA-4096 Dual Encryption](password-manager-using-aes-256-and-rsa-4096-dual-encryption.md)  **New Entry**

**Other**

22. [QR Code Generator](qr-code-generator.md)  **New Entry**
23. [Shortest Path Finder](shortest-path-finder.md)  **New Entry**
24. [Aim Trainer](aim-trainer.md)  **New Entry**
25. [Password Generator](password-generator.md)  **New Entry**
26. [Dictionary App](dictionary-app.md)
---

### 1. Calculator Program

A simple calculator that performs basic arithmetic operations:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (`%`)

#### Features:
- Handles division by zero gracefully.
- Accepts two numerical inputs from the user.
  
#### Example Usage:
```plaintext
Please select (+,-,*,/,%) : +
Number 1: 5
Number 2: 3
Result: 8
```

---

### 2. Weight Converter Program

Converts weight between kilograms and pounds.

#### Features:
- Input weight in either kilograms (K) or pounds (L).
- Accurate conversion using scientific constants.

#### Example Usage:
```plaintext
Enter Weight: 70
Kilograms or Pounds? (K/L): K
70 kilograms is equal to 154.32 pounds.
```

---

### 3. Temperature Converter Program

Converts temperatures between Celsius and Fahrenheit.

#### Features:
- Supports both directions of conversion.
- Provides clear and precise outputs.

#### Example Usage:
```plaintext
Is the temperature in Celsius or Fahrenheit? (C/F): C
Enter the temperature: 25
25°C is equal to 77.00°F.
```

---

### 4. Email Slicer Program

Extracts the username and domain from an email address.

#### Features:
- Simple and efficient slicing of email strings.

#### Example Usage:
```plaintext
Enter your Email: user@example.com
Your Username is user
Domain is example.com
```

---

### 5. Compound Interest Calculator Program

Calculates the compound interest on a given principal amount.

#### Features:
- Validates user input to ensure positive values.
- Provides the final balance after a specified time period.

#### Example Usage:
```plaintext
Enter Principle: 1000
Enter Rate: 5
Enter Time: 2
Balance after 2 years : $1102.50
```

---

### 6. Countdown Timer Program

Counts down from a specified number of seconds and displays the time in `HH:MM:SS` format.

#### Features:
- Dynamic formatting of time.
- Pauses execution between each decrement for realistic countdown.

#### Example Usage:
```plaintext
Enter the time in seconds : 10
00:00:10
00:00:09
...
TIME'S UP!
```

---

### 7. Shopping Cart Program

Simulates a shopping cart system where users can add items and calculate the total cost.

#### Features:
- Dynamically calculates the total price of items.
- Provides a neatly formatted receipt.

#### Example Usage:
```plaintext
Enter food items to buy (enter q to quit) : Apple
Enter the price of a Apple: $ 1.5
Enter food items to buy (enter q to quit) : q

-------- YOUR CART --------
Item                Price
------------------------------
Apple               $ 1.50
------------------------------
Total               $ 1.50
```

---

### 8. Quiz Game

A multiple-choice quiz game with questions on general knowledge.

#### Features:
- Supports up to 4 options for each question.
- Displays the correct answer for wrong attempts.
- Tracks and displays the final score.

#### Example Usage:
```plaintext
What is the capital of France?
a. Berlin
b. Madrid
c. Paris
d. Rome
Your choice (a, b, c, d): c
Correct!
```

---

### 9. Concession Stand Program

Simulates a concession stand where users can place orders from a menu.

#### Features:
- Displays a menu with items and their prices.
- Dynamically calculates the total cost based on the order.
- Provides a detailed receipt.

#### Example Usage:
```plaintext
Enter the item you want to order (or type 'done' to finish): Hot Dog
How many Hot Dog do you want? 2
Enter the item you want to order (or type 'done' to finish): done

------ Your Receipt ------
Item            Quantity    Price Each  Total Price
---------------------------------------------------
Hot Dog         2           $    3.50   $    7.00
---------------------------------------------------
Total Cost:                           $    7.00
--------------------------
```

---

### 10. Number Guessing Game

A fun game where the user guesses a randomly generated number between 1 and 100.

#### Features:
- Tracks the number of attempts.
- Provides hints for higher or lower guesses.

#### Example Usage:
```plaintext
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Guess a number between 1 and 100: 50
Too low!
Guess a number between 1 and 100: 75
Too high!
Guess a number between 1 and 100: 62
Correct! You guessed it in 3 attempts.
```

---

### 11. Rock-Paper-Scissors Game

## Overview
This Python program simulates a simple Rock-Paper-Scissors game where the player competes against the computer. The computer randomly selects a choice, and the result is determined based on standard game rules.

---

## How It Works
1. The computer randomly selects `rock`, `paper`, or `scissors` using the `random.choice()` function.
2. The player inputs their choice, which is validated to ensure it is one of `rock`, `paper`, or `scissors`.
3. The program compares the player’s choice with the computer’s choice to determine the winner based on:
   - Rock beats Scissors
   - Scissors beat Paper
   - Paper beats Rock
4. The result is displayed to the user.

---

## Example Run
```
Welcome to Rock, Paper, Scissors!
Choose 'rock', 'paper', or 'scissors'.
Enter your choice: rock
Computer chose: scissors
You win!
```

---
### 12. Dice Roller Program

## Overview
The Dice Roller Program is a simple Python application that simulates rolling dice. It generates random numbers for the dice rolls, displays their faces using ASCII art, and calculates the total sum of the rolls.

## Features
- Roll any number of dice specified by the user.
- Display dice rolls using visually accurate ASCII art.
- Calculate and display the total sum of all dice rolls.

## How It Works
1. The user inputs the number of dice to roll.
2. The program generates random values between 1 and 6 for each die.
3. Each die's face is displayed using pre-defined ASCII art.
4. The total of all rolled dice is calculated and displayed.

## Example Run
### Input
```
How Many Dice? : 3
```

### Output
```
┌─────────┐ ┌─────────┐ ┌─────────┐
│ ●       │ │ ●     ● │ │ ●  ●  ● │
│         │ │         │ │         │
│       ● │ │ ●     ● │ │ ●  ●  ● │
└─────────┘ └─────────┘ └─────────┘
Total: 13
```
### 13. Encryption and Decryption Program

This program encrypts and decrypts text using a randomized substitution cipher. It creates a shuffled key for encryption and uses it to both encrypt and decrypt messages.

## How It Works

1. **Character Mapping**:
   - A list of characters (`chars`) is created, including spaces, punctuation, digits, and letters (both uppercase and lowercase).
   - A shuffled copy of this list (`key`) is used to map characters for encryption and decryption.

2. **Encryption**:
   - For each character in the input text, its index in the `chars` list is determined.
   - The corresponding character from the `key` is appended to the encrypted message.

3. **Decryption**:
   - For each character in the encrypted text, its index in the `key` is determined.
   - The corresponding character from the `chars` list is appended to the decrypted message.


---

## Example Usage

### Encryption
**Input:**
```
Hello, World!
```
**Output:**
```
Encrypted Message: zJHG9@_t$eU!~
```

### Decryption
**Input:**
```
zJHG9@_t$eU!~
```
**Output:**
```
Decrypted Message: Hello, World!
```

---

## Features

- Supports spaces, punctuation, digits, and letters.
- Randomized encryption key ensures secure and unique ciphertexts.
- Reversible process guarantees accurate decryption.

---

## Limitations

- The encryption and decryption processes must use the same `key`. If the key is lost, the encrypted text cannot be decrypted.
- The program does not handle characters outside the defined `chars` list.

---

## Notes

- Ensure that the `key` remains consistent between encryption and decryption.
- To adapt for other character sets, modify the `chars` list accordingly.

---

## 14. Credit Card Validation Program

This program checks the validity of a credit card number using Luhn's Algorithm and determines the card type (e.g., AMEX, MasterCard, or VISA).

### How it Works:
1. **Luhn's Algorithm**:
   - Reverse the credit card number.
   - Double every second digit starting from the first reversed digit.
   - If the doubled number exceeds 9, subtract 9.
   - Sum all the digits.
   - If the total sum is divisible by 10, the card number is valid.

2. **Card Type Validation**:
   - **AMEX**: Length of 15 and starts with 34 or 37.
   - **MasterCard**: Length of 16 and starts with numbers 51 through 55.
   - **VISA**: Length of 13 or 16 and starts with 4.
---
### Example:
#### Input:
```
Enter your credit card number: 4111111111111111
```
#### Output:
```
VISA
```

---

## 15. Banking Program

This program simulates a simple banking system where users can view their balance, deposit money, and withdraw money.

### Features:
1. **Show Balance**: Display the current balance of the user.
2. **Deposit Money**: Add money to the user's account.
3. **Withdraw Money**: Remove money from the user's account, ensuring sufficient funds are available.
4. **Exit**: Exit the program.

---

### Example:
#### Menu:
```
Banking System Menu:
1. Show Balance
2. Deposit
3. Withdraw
4. Exit
```
#### Sample Interaction:
```
Enter your choice (1-4): 2
Enter the amount to deposit: 100
$100.00 deposited successfully.

Enter your choice (1-4): 1
Your current balance is: $100.00

Enter your choice (1-4): 3
Enter the amount to withdraw: 50
$50.00 withdrawn successfully.

Enter your choice (1-4): 4
Thank you for using our banking system. Goodbye!
```
# Upgraded Banking Program

## Overview
This program enhances the basic banking system by adding the following features:
- Account creation with encrypted passwords
- Secure login and authentication
- File-based storage for account information
- User account management (edit username, change password, delete account)

The program uses JSON for storing account data and provides a menu-driven interface for user interaction.

---

### 15.1. **Encryption and Decryption Functions**
The program secures user passwords using encryption:
- **Encrypt Password:** Encrypts a user's password using a shuffled character mapping.
- **Decrypt Password:** Decrypts the encrypted password using a reverse mapping.

### 2. **File Operations**
- **Save Account Info:** Stores all account details in a file named `accounts.txt` using JSON.
- **Load Account Info:** Loads account details from the `accounts.txt` file.

### 3. **Account Management**
- **Create Account:** Allows users to create a new account with a username and password.
- **Login:** Authenticates users by verifying their credentials.
- **Delete Account:** Deletes a user's account after verifying their credentials.
- **Edit Account:**
  - Change username.
  - Change password.

### 4. **Banking Operations**
- Show balance
- Deposit money
- Withdraw money

---

### 16. Slot Machine Program

This program simulates a simple slot machine game.

**How to Play:**

1. Run the program.
2. Press Enter to spin the slot machine.
3. The program will display three random emojis.
4. If all three emojis match, you win!
5. You can choose to play again or quit.

---
### 17. Hangman Game

This program implements a classic text-based Hangman game.

**How to Play:**

1. The game randomly selects a word from a predefined list.
2. You are presented with a series of underscores representing the hidden word.
3. You guess letters one at a time.
4. If your guess is correct, the letter is revealed in the word.
5. If your guess is incorrect, you lose a life (represented by the hangman drawing).
6. You have a limited number of attempts to guess the word.
7. If you guess the word correctly before running out of attempts, you win!

---

### 18. Digital Clock Program using PyQt5

This project implements a simple digital clock application using the PyQt5 library.

**Features:**

* Displays the current time in a user-friendly format (HH:mm:ss).
* Runs continuously, updating the time every second.
* Customizable appearance with a dark background and white text.

     
---

### 19. Stopwatch Program using PyQt5

This project creates a simple stopwatch application with start/stop functionality using the PyQt5 library.

**Features:**

* Displays the elapsed time in hours, minutes, and seconds format (HH:mm:ss).
* Starts, stops, and resets the stopwatch using a single button.
* Customizable appearance with a dark background and white text.

---
 
### 20. Weather App with PyQt5

This project creates a desktop weather application using the PyQt5 library and OpenWeatherMap API.

**Features:**

* Enter a city name and retrieve the current weather information (temperature and description).
* Displays the temperature in Celsius (°C).
* Shows a relevant weather emoji based on the weather description.
* Implements dark and light theme options.

---

### 21. Password Manager with Dual Encryption

This secure password manager utilizes a combination of AES-256 symmetric-key encryption and RSA-4096 public-key encryption to safeguard your usernames and passwords.

**Features:**

* Encrypts data at rest using AES-256 for robust protection.
* Employs RSA-4096 for additional security during key storage.
* Enables creation of multiple accounts, each secured by a unique master password.
* Allows storing usernames and passwords for various platforms within each account.
* Provides functionalities for viewing, adding, deleting, and editing platform data.

---   

### 22. QR Code Generator - PyQt5 Application

This user-friendly QR code generator application allows you to create QR codes from text or URLs with a sleek and customizable interface.

**Features:**

* Generates QR codes from user-provided text or URLs.
* Saves generated QR codes in PNG and SVG formats for versatility.
* Employs a dark theme for a visually appealing experience.
* Provides clear instructions and status updates for ease of use.
* Offers customization options through a stylesheet (optional).

---
### 23. Shortest Path Finder - PyQt5 Application

This interactive application utilizes the A* search algorithm to visually demonstrate the process of finding the shortest path within a maze.

**Features:**

* Provides a customizable maze layout.
* Employs a user-friendly interface with a dark theme for better visualization.
* Animates the path finding process, highlighting the explored paths step-by-step.
* Identifies all possible shortest paths from the starting point to the destination.

---
### 24. Aim Trainer - Improve Your Clicking Accuracy

This interactive application helps you hone your clicking accuracy and reflexes through a challenging and engaging aim training experience.

**Features:**

* Spawns randomly sized targets at varying intervals to test your reaction time and precision.
* Tracks your performance metrics, including time elapsed, targets clicked, clicks made, and accuracy.
* Provides a visual top bar that displays your current performance statistics.
* Ends the training session when you miss a certain number of targets, presenting a summary screen with your final results.

   
### 25. Strong Password Generator - Create Secure Passwords with Ease

This user-friendly application empowers you to generate robust passwords that enhance your online security.

**Features:**

* **Strong Password Generation:** Creates complex passwords by incorporating a mix of uppercase and lowercase letters, numbers, and symbols.
* **Customization:** Leverages the user's input string to strengthen existing passwords, making them more secure.
* **Intuitive Interface:** Provides a clear and well-organized layout with informative labels and buttons for a seamless user experience.
* **Dark Mode Support:** Offers a visually appealing dark theme that reduces eye strain and complements modern aesthetics (optional).

 
---

### 26. Dictionary App - Explore Word Meanings with Ease

This user-friendly application serves as your personal digital dictionary, empowering you to look up word definitions conveniently and efficiently.

**Features:**

* **Meaning Lookups:** Effortlessly search for the meaning of any word using the intuitive search bar.
* **Comprehensive Results:** Retrieves detailed definitions from a trusted online dictionary, providing a clear understanding of word usage.
* **Part-of-Speech Identification:** Distinguishes between different grammatical functions (e.g., noun, verb, adjective) associated with the searched word, enhancing clarity.
* **Dark Mode Support:** Offers an optional dark theme that reduces eye strain and provides a visually appealing interface.

---

