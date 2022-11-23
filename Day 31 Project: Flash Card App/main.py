import tkinter as tk
import pandas as pd
import random 

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    words_list = data.to_dict(orient= "records")


current_card = {}

def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_list)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"] , fill="black")    
    canvas.itemconfig(canvas_image, image = card_front_img)
    flip_timer = window.after(3000, func=flip_card)

    
def flip_card():
    canvas.itemconfig(canvas_image, image = card_back_img)
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill="white")

def is_known():
    words_list.remove(current_card)
    random_card()
    
    
    data = pd.DataFrame(words_list)    
    data.to_csv('data/words_to_learn.csv', index = False)

window = tk.Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
check_img = tk.PhotoImage(file="images/right.png")
cross_img = tk.PhotoImage(file="images/wrong.png")

canvas = tk.Canvas(width=800, height=400, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image = card_front_img )
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text ="title", font=("Ariel", 40, "italic"))
card_word  = canvas.create_text(400, 263, text ="word", font=("Ariel", 60, "bold"))

know_button = tk.Button(image=check_img, highlightthickness=0, command= is_known)
unknow_button = tk.Button(image=cross_img, highlightthickness=0, command= random_card)
know_button.grid(row=1, column=1)
unknow_button.grid(row=1, column=0)

flip_timer = window.after(3000, func=flip_card)

random_card()

window.mainloop()
