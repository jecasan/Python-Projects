from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 10)

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.label = Label(text=f"Score = {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Text", 
            font=QUESTION_FONT, 
            fill=THEME_COLOR)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)
        
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, command=self.answer_true, highlightthickness=0)
        self.true_button.grid(column=0, row=2)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, command=self.answer_false, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score = {self.quiz.score}") 
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def answer_true(self):
        self.check_answer("True")   
        
    def answer_false(self):
        self.check_answer("False")
        
    def check_answer(self, answer):
        result = self.quiz.check_answer(answer)
        if result:
            self.canvas.config(bg="green")    
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
            

    