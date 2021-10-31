from tkinter import *
from quiz_brain import QuizBrain


class QuizUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz Game')
        self.window.config(padx=20, pady=20, bg='orange')

        self.score_label = Label(text=f'Score: {self.quiz.score}', fg='black', bg='orange',
                                 font=('Arial', 15, 'normal'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text=f"{self.quiz.next_question}",
                                                     fill='black',
                                                     font=('Arial', 15, 'normal'))
        self.canvas.grid(row=1, column=1, columnspan=2, pady=50)

        true_image = PhotoImage(file='images/check.png')
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0, bg='orange',
                                  command=self.answer_true)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file='images/remove.png')
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, bg='orange',
                                   command=self.answer_false)
        self.false_button.grid(row=2, column=2)

        self.get_new_question()

        self.window.mainloop()

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('true', self.quiz.current_question.answer))

    def answer_false(self):
        is_right = self.quiz.check_answer('false', self.quiz.current_question.answer)
        self.give_feedback(is_right)

    def get_new_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f'You reached the end of the game! Final score: {self.quiz.score}/{self.quiz.question_number}')
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_new_question)
