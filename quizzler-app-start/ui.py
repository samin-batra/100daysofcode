from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(height=500, width=400, bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", font=("Ariel", 10, "normal"), bg=THEME_COLOR, foreground='white')
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white", bd=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 124,
                                                     text="Question goes here",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Ariel", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)
        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.pressed_false)
        self.button_false.config(pady=20)
        self.button_false.grid(row=2, column=1)
        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.pressed_true)
        self.button_true.config(pady=20)
        self.button_true.grid(row=2, column=0)
        self.quiz = quiz_brain
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q)
        else:
            self.canvas.itemconfig(self.question_text, text = "No more questions left!")
            self.button_true.config(state = "disabled")
            self.button_false.config(state = "disabled")

    def pressed_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # self.get_next_question()

    def pressed_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        # self.get_next_question()

    def give_feedback(self, is_right: bool):
        if is_right:
            self.score+=1
            self.canvas.config(bg = "green")
            self.score_label.config(text = f"Score: {self.score}")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000, self.get_next_question)


    def change_color(self, color: str):
        self.canvas.config(bg = color)
