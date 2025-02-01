# Putting the card front image into the window
from tkinter import* 
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")

# Putting the image at center point, to fill uniformly
canvas.create_image(400,263, image= card_front_img)
canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"),fill="black")
canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"),fill = "black")

# Changing bgcolor of image to avoid discoloured thickness 
canvas.config(bg=BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row=0, column=0)



window.mainloop()