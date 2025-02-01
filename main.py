# Putting the card front image into the window
from tkinter import* 
import pandas as pd, random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
french2eng = {}

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    french2eng = original_data.to_dict(orient = "records")
else:
    french2eng = data.to_dict(orient="records")


def next_card():
    # Making it global to acceess this outside next_card()
    global current_card, flip_timer
    # Every time we get inside a new card, we will invalidate the flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french2eng)
    canvas.itemconfig(card_title, text= "French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image= card_front_img)
    # Flip card after 3 seconds
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    canvas.itemconfig(card_title, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= current_card["English"], fill= "white")
    canvas.itemconfig(card_background, image= card_back_img)

def is_known():
    # Removes current card from the cards in the list of word_to_learn
    french2eng.remove(current_card)
    print(len(french2eng))
    data = pd.DataFrame(french2eng)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
# Flip card after 3 seconds
flip_timer = window.after(3000, func= flip_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file= "card_front.png")
card_back_img = PhotoImage(file= "card_back.png")

# Putting the image at center point, to fill uniformly
card_background = canvas.create_image(400,263, image= card_front_img)
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
right_button = Button(image= right_image, highlightthickness=0, command= is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()