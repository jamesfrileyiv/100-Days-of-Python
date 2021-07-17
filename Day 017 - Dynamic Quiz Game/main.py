from quiz_brain import QuizBrain

quiz = QuizBrain()
quiz.ask_questions()
print("You completed the quiz.")
print(f"Your final score was {quiz.get_final_score()}%.")
