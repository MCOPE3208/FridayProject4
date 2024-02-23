import random

# Define a dictionary with questions as keys and correct answers as values
test_questions = {
    "What is the third planet from the sun?": "Earth",
    "How many hearts does an octopus have? A:3 B:10 C:1": "A",
    "Where does the Wizard live in The Wizard of Oz?": "Emerald City",
    "The Titanic sank in 1912: (T/F)": "T",
    "What sport is played at Wimbledon? A:Basketball B:Lacrosse C:Tennis": "C",
    # Add more questions as needed
}

def display_question(question):
    print(question)

def main():
    print("Welcome to the Quizbowl Program!")

    score = 0  # Initialize the user's score

    for question, correct_answer in test_questions.items():
        display_question(question)  # Display the current question
        user_answer = input("Your answer: ").strip()

        # Check if the user's answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Well done.\n")
            score += 1  # Increment the user's score for a correct answer
        else:
            print(f"Sorry, the correct answer is: {correct_answer}\n")

    print(f"\nYour final score is: {score}/{len(test_questions)}")
    print("Thanks for using the Quizbowl Program. Goodbye!")

if __name__ == "__main__":
    main()
