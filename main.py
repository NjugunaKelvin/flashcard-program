from tkinter import *
import pandas
import random

BACKGROUND = "#00008B"

current_card = {}

to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # create a dictionary
    to_learn = data.to_dict(orient="records")

# print(data)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French "])
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French "])
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, bg=BACKGROUND)


flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/front.png")

card_back = PhotoImage(file="images/back.png")

card_bg = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 24, "italic"))

card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


canvas.config(background=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)



next_card()

window.mainloop()