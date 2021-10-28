from tkinter import *

window = Tk()

window.title('Mi to Km App')
window.minsize(height=300, width=400)

# create texts
my_label = Label(text='Miles to Kilometers App', font=('Arial', 20, 'normal'))
my_label.pack()


# my_label['text'] = 'New Text'
# my_label.config(text='text')

# create buttons
def button_clicked():
    my_label['text'] = calc_input.get()


button = Button(text='click me', command=button_clicked)
button.pack()

# create input fields
calc_input = Entry(width=10)
calc_input.pack()
calc_input.get()

window.mainloop()
