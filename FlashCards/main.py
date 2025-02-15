import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

#---------------------------Word Generator---------------------------#
try:
    data = pandas.read_csv("words_to_learn.csv", encoding='unicode_escape')
except FileNotFoundError:
    data = pandas.read_csv("german_english.csv", encoding='unicode_escape')

to_learn = data.to_dict(orient="records")
current_word = {}    

def new_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_word["German"], fill="black") 
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, flip_card)
              
def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    
def remove_card():
    to_learn.remove(current_word)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)
    new_card() 
#---------------------------UI---------------------------#
window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

right_img = tk.PhotoImage(file="images/right.png")
wrong_img = tk.PhotoImage(file="images/wrong.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_front_img = tk.PhotoImage(file="images/card_front.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(column=0, columnspan=2, row=0)

right_button = tk.Button(image=right_img, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=1)

wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

new_card()


window.mainloop()