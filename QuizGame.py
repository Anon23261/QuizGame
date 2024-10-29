import random

def display_intro():
    print("Welcome to the Python Quiz Game!")
    print("Test your Python knowledge with multiple-choice questions.")
    print("Try to get as many correct as you can!\n")

def get_questions():
    # List of quiz questions, each with a question, options, and the correct answer index
    return [
        {
            "question": "What is the correct way to define a function in Python?",
            "options": ["A) function myFunc()", "B) def myFunc():", "C) func myFunc()", "D) myFunc def()"],
            "answer": 1  # This is the index of the correct answer in the options list
        },
        {
            "question": "Which data type is mutable in Python?",
            "options": ["A) tuple", "B) string", "C) list", "D) integer"],
            "answer": 2
        },
        {
            "question": "How do you insert a comment in Python code?",
            "options": ["A) // this is a comment", "B) /* this is a comment */", "C) # this is a comment", "D) <!-- this is a comment -->"],
            "answer": 2
        },
        {
            "question": "What is the output of '2' + '3' in Python?",
            "options": ["A) 5", "B) 23", "C) Error", "D) None of the above"],
            "answer": 1
        },
        {
            "question": "What keyword is used to start a loop in Python?",
            "options": ["A) loop", "B) iterate", "C) for", "D) repeat"],
            "answer": 2
        }
    ]

def ask_question(question_data):
    # Display the question and possible answers
    print(question_data["question"])
    for i, option in enumerate(question_data["options"]):
        print(f"  {option}")

    # Get user's answer
    while True:
        try:
            answer = int(input("Enter the number of your answer (1-4): ")) - 1
            if 0 <= answer <= 3:
                return answer == question_data["answer"]  # Return True if correct
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz():
    questions = get_questions()
    random.shuffle(questions)  # Shuffle questions for variety
    score = 0

    for question_data in questions:
        print("\n" + "-" * 50)
        if ask_question(question_data):
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer was {question_data['options'][question_data['answer']]}")
    
    print("\nQuiz Complete!")
    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent job! You got all answers correct!")
    elif score > len(questions) // 2:
        print("Good effort! Keep practicing to improve.")
    else:
        print("Don't worry, keep studying and try again!")

# Game execution starts here
if __name__ == "__main__":
    display_intro()
    run_quiz()
