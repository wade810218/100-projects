import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text = "Score: 0", fg="white",bg=THEME_COLOR)
        self.canvas = tk.Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,  
                                    width=280, text="Quote Goes HERE", 
                                    font=("Arial", 20, "italic"), fill=THEME_COLOR )

        true_image = tk.PhotoImage(file="images/true.png")
        false_image = tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, 
                                     command=self.true_pressed)
        self.false_button = tk.Button(image=false_image, highlightthickness=0, 
                                      command=self.false_pressed)
        #self.window.minsize(width=500, height=300)
        
        self.score_label.grid(row=0,column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady = 50)
        
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            
            self.score_label.config(text= f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question )
        
