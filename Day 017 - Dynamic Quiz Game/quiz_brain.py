import html
import requests
from question_model import Question


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.questions_list = self.initialize_questions()
        self.correct_answers = 0

    @staticmethod
    def query_questions():
        """Makes API GET Request to Open Trivia DB to retrieve ten questions. Returns questions properly formatted for
        processing into Question Objects"""
        r = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        question_data = []
        for result in r.json()['results']:
            question = {
                'text': html.unescape(result['question']),
                'answer': result['correct_answer']
            }
            question_data.append(question)
        return question_data

    def initialize_questions(self):
        """reads question data and returns a list of question objects"""
        qb = []
        question_data = self.query_questions()
        for question in question_data:
            new_question = Question(question['text'], question['answer'])
            qb.append(new_question)
        return qb

    def ask_questions(self):
        """Asks all questions in quiz, retrieves answers, and evaluates answers"""
        while self.check_end():
            print(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)?")
            answer = self.get_answer()
            self.evaluate_answer(self.questions_list[self.question_number], answer)
            print()

    @staticmethod
    def get_answer():
        """"Returns user's answer with built in error checking."""
        answer = ""
        invalid_input = answer not in ["true", "false"]
        while invalid_input:
            answer = input("> ").lower()
            invalid_input = answer not in ["true", "false"]
            if invalid_input:
                print("Please enter true or false.")

        return answer

    def evaluate_answer(self, question, answer):
        """"Evaluates answer and prints current score"""
        if answer.lower() == question.answer.lower():
            print("Correct!")
            self.correct_answers += 1
        else:
            print(f"Sorry, that is incorrect. The correct answer is {question.answer}")
        self.print_current_score()
        self.question_number += 1

    def print_current_score(self):
        """Prints current score. Is called by self.evaluate_answer method"""
        print(f"Your current score is {self.correct_answers} / {self.question_number+1}.")

    def get_final_score(self):
        """Calculates and returns final score"""
        final_score = round((self.correct_answers / len(self.questions_list)) * 100, 2)
        return final_score

    def check_end(self):
        """Checks if quiz is at the end of questions list. Returns true if not at the end, else false"""
        return self.question_number < len(self.questions_list)
