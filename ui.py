from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="text here",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/right.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/wrong.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = f"You have reached the end of the quiz!\n\nYour final score is {self.quiz.score}/10."
            self.score_label.destroy()
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
