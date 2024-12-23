def ask_question(question, options, correct_option):
    print(question)
    # Display options with labels a, b, c, d
    for i, option in enumerate(options, start=1):
        print(f"{chr(96 + i)}. {option}")

    while True:
        answer = input("Your choice (a, b, c, d): ").strip().lower()
        if answer in ('a', 'b', 'c', 'd'):
            break
        else:
            print("Invalid input. Please enter a, b, c, or d.")

    # Convert answer to index (0-3)
    index = ord(answer) - 97
    if options[index].lower() == correct_option.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_option}\n")
        return False

def question_game():
    print("Welcome to the Question Game!")
    print("Answer the following questions by choosing the correct option:\n")

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ("Berlin", "Madrid", "Paris", "Rome"),
            "answer": "Paris"
        },
        {
            "question": "What is 5 + 7?",
            "options": ("10", "11", "12", "13"),
            "answer": "12"
        },
        {
            "question": "What is the color of the sky on a clear day?",
            "options": ("Green", "Blue", "Red", "Yellow"),
            "answer": "Blue"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ("Charles Dickens", "Leo Tolstoy", "William Shakespeare", "Mark Twain"),
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ("Earth", "Jupiter", "Mars", "Venus"),
            "answer": "Jupiter"
        }
    ]

    score = 0

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print("Game over!")
    print(f"Your final score is: {score}/{len(questions)}")

# Start the game
question_game()
