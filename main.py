from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
#---------RANDOM FUNCTION--------
to_learn = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn )
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=image_used_front)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title,text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"], fill="white")
    canvas.itemconfig(card_background,image=image_used_back)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()
#----------UI INTERFACE ------------
window = Tk()
window.title("FLASH CARD")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
#FLIP THE CARD
flip_timer= window.after(3000,func=flip_card)
#CARD FRONT
canvas = Canvas(width=800, height=526)
image_used_front = PhotoImage(file="images/card_front.png")
image_used_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=image_used_front)
card_title = canvas.create_text(400,150,text="title",font=("Ariel",24,"italic"))
card_word = canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)

#right button
image_right = PhotoImage(file="images/right.png")
button1 = Button(image=image_right,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=is_known)
button1.grid(column=1,row=1)

#wrong button
image_wrong= PhotoImage(file="images/wrong.png")
button2=Button(image=image_wrong,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=next_card )
button2.grid(column=0,row=1)

next_card()

window.mainloop()