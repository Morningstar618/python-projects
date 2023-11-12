from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        ############## UI START ##################
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.ques_text = self.canvas.create_text(150, 125, text="Some Text", font=("Arial", 15, "italic"), width=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.question_right)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.question_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
        ############### UI END ###################


    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text, text="You have reached the end of the quiz!")
            self.true_button.configure(state="disabled")
            self.false_button.configure(state="disabled")


    def question_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def question_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)

