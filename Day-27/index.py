import sys

# Define questions and answers using a list of tuples
questions = [
    ("What is the capital of France?", "Paris"),
    ("Who wrote 'Pride and Prejudice'?", "Jane Austen"),
    ("What is the chemical symbol for water?", "H2O"),
    ("Which planet is known as the Red Planet?", "Mars"),
    ("What is the currency of Japan?", "Yen")
]

def display_question(question_number, question):
    """Display a single question."""
    print(f"Question {question_number}: {question}")

def get_user_answer():
    """Get user input for the answer."""
    return input("Your answer: ").strip()

def play_game():
    """Play the quiz game."""
    total_amount = 0
    for i, (question, correct_answer) in enumerate(questions, start=1):
        display_question(i, question)
        user_answer = get_user_answer()
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            total_amount += 1000  # Increment amount for each correct answer
        else:
            print("Incorrect!")
            break  # End the game if the answer is incorrect
    return total_amount

def main():
    print("Welcome to the Quiz Game!")
    print("Answer the questions correctly to win money.")
    print("You will get $1000 for each correct answer.")
    print("You can quit anytime by typing 'quit'.\n")
    
    total_won = play_game()
    print(f"\nCongratulations! You won a total of ${total_won}.")

if __name__ == "__main__":
    main()
