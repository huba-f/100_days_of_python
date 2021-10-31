from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUi

question_bank = []

for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer']))

quiz = QuizBrain(question_bank)
quiz_ui = QuizUi(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()
print('you completed the quiz!')
print(f'your final score is {quiz.score}/{quiz.question_number}.')
