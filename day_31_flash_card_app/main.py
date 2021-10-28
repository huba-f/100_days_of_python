from tkinter import *
import pandas
import random

# ----------- CONSTANTS ----------- #
BACKGROUND_COLOR = '#c7ffd5'

# ----------- EXTRACTING DATA ----------- #

data = pandas.read_csv('data/most_used_words - Sheet1.csv')
to_learn = data.to_dict(orient='records')


# ----------- BRAIN ----------- #


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(english_text, text=current_card['En'])
    canvas.itemconfig(magyar_text, text=current_card['Hu'])


# ----------- UI ----------- #
window = Tk()
window.title('most used korean words')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=800)
flash_card = PhotoImage(file='media/flashcard.png')
canvas.create_image(400, 400, image=flash_card)
# english text
english_text = canvas.create_text(400, 230, text=f'', font=('Ariel', 40, 'italic'))

# magyar text
magyar_text = canvas.create_text(400, 590, text=f'', font=('Ariel', 40, 'italic'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1)

cross_image = PhotoImage(file='media/wrong_button.png')
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
unknown_button.grid(row=0, column=0)

checkmark_image = PhotoImage(file='media/right_button.png')
known_button = Button(image=checkmark_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0,
                      command=next_card)
known_button.grid(row=0, column=2)

next_card()

window.mainloop()
