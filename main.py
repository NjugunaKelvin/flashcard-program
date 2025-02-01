from tkinter import *



BACKGROUND = "#00008B"
window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/front.png")
canvas.create_image(400, 263, image=card_front)

canvas.create_text(400, 150, text="Title", font=("Arial", 24, "italic"))

canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))


canvas.config(background=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)





window.mainloop()