from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_XCOR = 400
FRENCH_YCOR = 150
ENGLISH_YCOR = 263
FRENCH_FONT = ("Ariel", 40, "italic")
ENGLISH_FONT = ("Ariel", 40, "bold")

french_words = None
render_words = None
displayed_word = {}

def read_words_from_file():
    global french_words, render_words
    try:
        french_words = pd.read_csv("data/words_to_learn.csv")
    except:
        french_words = pd.read_csv("data/french_words.csv")
    finally:
        render_words = french_words.to_dict(orient = "records")


def generate_new_word():
    read_words_from_file()
    global flip_timer, render_words
    window.after_cancel(flip_timer)
    word = random.choice(render_words)
    global displayed_word
    displayed_word = word
    # word = render_words['French'][key]
    canvas_card.itemconfig(canvas_image, image = front_image)
    canvas_card.itemconfig(french_text, text = displayed_word['French'], fill = 'black')
    canvas_card.itemconfig(lang_text, text = "French", fill = "black")
    window.after(3000, func=flip_image)


def flip_image():
    global  displayed_word
    canvas_card.itemconfig(canvas_image, image = back_image)
    canvas_card.itemconfig(french_text, text = displayed_word['English'], fill = "white")
    canvas_card.itemconfig(lang_text, text = "English", fill = "white")


def update_file():
    global render_words, displayed_word
    render_words.remove(displayed_word)
    data_to_write = pd.DataFrame(render_words)
    print(data_to_write)
    data_to_write.to_csv("data/words_to_learn.csv",columns = ['French','English'], header = True, index = False)
    generate_new_word()


window = Tk()
window.title("Flash Card")
read_words_from_file()
window.config(height=626, width=900, padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_image)
canvas_card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0)
canvas_card.grid(row=0, column=0, columnspan=2)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas_card.create_image(400, 263, image=front_image)

lang_text = canvas_card.create_text(FRENCH_XCOR, FRENCH_YCOR, text="", font=FRENCH_FONT)

french_text = canvas_card.create_text(FRENCH_XCOR, ENGLISH_YCOR, text="", font=ENGLISH_FONT)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command = generate_new_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command = update_file)
right_button.grid(row=1, column=1)
# button_no = Button()

generate_new_word()

window.mainloop()
