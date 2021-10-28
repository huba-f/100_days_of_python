from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import json

FONT_NAME = "Courier"


# ----------------------- PASSWORD GENERATOR ----------------------- #
def pass_password():
    password = generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)


# ----------------------- SEARCH ----------------------- #
def search():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]['username']
                password = data[website]['password']
                messagebox.showinfo(title=f'{website}', message=f'username: {email}\npassword: {password}')
            else:
                messagebox.showinfo(title=f'{website}', message=f'"{website}" not found.')
    except FileNotFoundError:
        messagebox.showinfo(title=f'No data found', message=f'no saved passwords yet')


# ----------------------- SAVE PASSWORD ----------------------- #

def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'username': username,
            'password': password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='hey fuck face!', message='enter something!')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update new_data
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(message='done.')


# ----------------------- UI SETUP ----------------------- #

# creating window
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50, bg='white')

# creating canvas
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)

# adding image
lock_image = PhotoImage(file='lock.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# creating input fields and belonging text


# -- website field -- #

# text
website_label = Label(text='website:', font=(FONT_NAME, 14), bg='white')
website_label.grid(row=1, column=0)

# input
website_input = Entry(width=25)
website_input.grid(row=1, column=1)
website_input.focus()

# button
search_button = Button(text='search', bg='#f0f0f0', width='7', command=search)
search_button.grid(row=1, column=2, columnspan=2)

# -- email/username field -- #

# text
username_label = Label(text='email/username:', font=(FONT_NAME, 14), bg='white')
username_label.grid(row=2, column=0)

# input
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, 'huba0ferencz@gmail.com')

# -- password field -- #

# text
password_label = Label(text='password:', font=(FONT_NAME, 14), bg='white')
password_label.grid(row=3, column=0)

# output
password_input = Entry(width=25)
password_input.grid(row=3, column=1)

# button
generate_button = Button(text='generate', bg='#f0f0f0', command=pass_password, width=7)
generate_button.grid(row=3, column=2, columnspan=2)

# -- submit field -- #

# button

add_button = Button(text='add', width=32, bg='#f0f0f0', command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
