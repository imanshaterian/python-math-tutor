import random
import time

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    print("Welcome to the Multiplication Tables Practice!")
    
    num_questions = get_positive_integer("Enter the number of practice questions: ")
    max_number = get_positive_integer("Enter the highest number to be used in questions: ")
    
    questions = []
    correct_answers = 0
    
    start_time = time.time()
    
    for _ in range(num_questions):
        a = random.randint(1, max_number)
        b = random.randint(1, max_number)
        correct_answer = a * b
        user_answer = int(input(f"What is {a} x {b}? "))
        
        questions.append((a, b, user_answer, correct_answer))
        
        if user_answer == correct_answer:
            correct_answers += 1
    
    end_time = time.time()
    total_time = end_time - start_time
    avg_time_per_question = total_time / num_questions
    
    # Display results
    print("\nThanks for playing!")
    print(f"Number of correct answers: {correct_answers} / {num_questions}")
    print(f"Percentage correct: {correct_answers / num_questions * 100:.2f}%")
    print(f"Total time taken: {total_time:.2f} seconds")
    print(f"Average time per question: {avg_time_per_question:.2f} seconds")
    
    # Display all questions and answers
    print("\nHere are all the questions and your answers:")
    for q in questions:
        a, b, user_answer, correct_answer = q
        result = "Correct" if user_answer == correct_answer else "Incorrect"
        print(f"{a} x {b} = {user_answer} (Correct answer: {correct_answer}) - {result}")

if __name__ == "__main__":
    main()
