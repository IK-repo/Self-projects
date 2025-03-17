def run_question_game():
    # Define questions, answers, and maximum tries for each question
    questions = [
        {
            "question": "What is the capital of France?",
            "answer": "paris",
            "max_tries": 3
        },
        {
            "question": "What is 2 + 2?",
            "answer": "4",
            "max_tries": 2
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "jupiter",
            "max_tries": 3
        }
    ]
    
    # Loop through each question
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        
        # Initialize tries for this question
        tries_left = q['max_tries']
        
        # Loop until correct answer or out of tries
        while tries_left > 0:
            # Get user input
            user_answer = input(f"Your answer ({tries_left} tries remaining): ").lower().strip()
            
            # Check if answer is correct
            if user_answer == q['answer']:
                print("Correct! Moving to next question.")
                break
            else:
                tries_left -= 1
                
                # Check if out of tries
                if tries_left == 0:
                    print("\nGame Over! You ran out of tries.")
                    return
                else:
                    print(f"Incorrect. Try again!")
        
        # If we get here, the answer was correct, so continue to next question
    
    # If we get here, all questions were answered correctly
    print("\nCongratulations! You completed all questions correctly!")

# Run the game
run_question_game()
