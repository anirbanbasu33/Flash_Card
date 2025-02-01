# Putting the card front image into the window
from tkinter import* 
import pandas as pd, random
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("french_words.csv")
# converts dataframe into a list of dictionaries (refer test.py)
french2eng = df.to_dict(orient="records")
def next_card():

    # This inputs a dictionary element from the list of dictionaries
    current_card = random.choice(french2eng)
    canvas.itemconfig(card_title, text= "French")
    canvas.itemconfig(card_word, text=current_card["French"])

window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")

# Putting the image at center point, to fill uniformly
canvas.create_image(400,263, image= card_front_img)
card_title = canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"),fill="black")
card_word = canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"),fill = "black")

# Changing bgcolor of image to avoid discoloured thickness 
canvas.config(bg=BACKGROUND_COLOR, highlightthickness = 0)
# columnspan=2, So that the upperpart is seperated and below part can be put to grid properly
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file= "wrong.png")
wrong_button = Button(image= wrong_image, highlightthickness=0, command= next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file= "right.png")
right_button = Button(image= right_image, highlightthickness=0, command= next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()