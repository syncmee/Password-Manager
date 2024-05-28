import json
from tkinter import *
from random import *
from tkinter import messagebox
from json import *
import pyperclip

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
    pyperclip.copy(password)

#save-password
def save():
    web = website_entry.get()
    mail = mail_entry.get()
    pw = password_entry.get()
    data_info = {
        web: {
            "email": mail,
            "password":pw
        }
    }
    if len(web) == 0 or len(mail) == 0 or len(pw) == 0:
        messagebox.showerror(title="Error",message="Fields are empty. "
                                                   "\nPlease fill all the details before saving.")
    else:
        isok = messagebox.askokcancel(title=web,message=f"These are the details entered \nEmail:{mail} \nPassword:{pw} "                                               f"\nDo you want to continue?")
        if isok:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(data_info)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file,indent=4)

            website_entry.delete(0, 'end')
            mail_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
def search():
    with open("data.json", mode="r") as data_file:
        data = json.load(data_file)
        web = website_entry.get()
        x = data[web]
        mail = x["email"]
        pw = x["password"]

    web = website_entry.get()
    messagebox.showinfo(title=web, message=f"Email:{mail} \nPassword:{pw}")




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
add = Button(text="Add",width=35,command=save)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search",width=15,command=search)
search.grid(column=2,row=1)

### Text-Inputs
website_entry = Entry(width=22)
website_entry.grid(row=1,column=1)
website_entry.focus()
mail_entry = Entry(width=41)
mail_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=22)
password_entry.grid(row=3,column=1)






window.mainloop()