from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
QUIZ_FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_title = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="White")
        self.score_title.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question = self.canvas.create_text(150, 125,
                                                width=280,
                                                text="d",
                                                font=QUIZ_FONT,
                                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, background=THEME_COLOR, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, background=THEME_COLOR, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_title.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback("is_right")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)