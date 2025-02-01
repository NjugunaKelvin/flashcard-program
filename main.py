from tkinter import *



BACKGROUND = "#B1DDC6"
window = Tk()
window.title("Learn French")
window.config(padx=50, pady=50, bg=BACKGROUND)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/front.png")
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0)



window.mainloop()