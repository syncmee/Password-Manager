from tkinter import *
from random import *

#password-generator
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []


def generatepass():
    import random
    global password_list
    for char in range(1, 5):
        password_list.append(random.choice(letters))
    for char in range(1, 5):
        password_list += random.choice(symbols)
    for char in range(1, 5):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)

#save-password
def save():
    web = website_entry.get()
    mail = mail_entry.get()
    pw = password_entry.get()
    with open("data.txt", mode="a") as data:
        data.writelines(f"{web} | {mail} | {pw}")
    website_entry.delete(0, 'end')
    mail_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

#gui
### Window
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

### Logo
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image= img)
canvas.grid(row=0,column=1)

### Label
website = Label(text="Website:")
website.grid(column=0,row=1)

mail_username = Label(text="Email/Username:")
mail_username.grid(column=0,row=2)

password = Label(text="Password:")
password.grid(column=0,row=3)

### Buttons
generate = Button(text="Generate Password",command=generatepass)
generate.grid(column=2, row=3)
add = Button(text="Add",width=36,command=save)
add.grid(column=1, row=4, columnspan=2)

### Text-Inputs
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
mail_entry = Entry(width=35)
mail_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)






window.mainloop()