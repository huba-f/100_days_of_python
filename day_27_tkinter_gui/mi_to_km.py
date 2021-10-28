from tkinter import *

default_output = 'mi'
window = Tk()

window.title('Mi to Km App')
window.geometry('300x300')

# create texts
app_name = Label(text='.', font=('Arial', 1, 'normal'))
app_name.pack()

# create input fields
calc_input = Entry(width=10)
calc_input.pack(pady=(30, 10))
calc_input.get()

# calc_input.insert(END, string="km")
equal_sign = Label(text='=', font=('Arial', 20, 'normal'))
equal_sign.pack()

calc_output = Entry(width=10)
calc_output.pack()
calc_output.get()


# calc_output.insert(END, string=default_output)


# create buttons
def clear():
    calc_input.delete(0, 'end')
    calc_output.delete(0, 'end')


def calculate():
    # if type(calc_output) == int:
    #     num = int(calc_output.get())
    #     num *= 1.609
    #     str(num)
    #     calc_input.insert(END, string=num)
    if calc_input and calc_output != '':
        num = int(calc_input.get())
        num /= 1.609
        str(num)
        calc_output.insert(END, string=num)
        calc_input.delete(END)
    else:
        return


calc_button = Button(text='calculate', command=calculate)
calc_button.pack(pady=(10, 10))

clear_button = Button(text='clear', command=clear)
clear_button.pack(pady=(10, 10))

window.mainloop()
