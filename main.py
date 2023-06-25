from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import random
import json


def generate_password():
    # password generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)

    nr_numbers = random.randint(2, 4)
    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_g = ""
    for char in password_list:
        password_g += char

    entry_3.insert(0, password_g)


def save():
    new_data = {
        entry_1.get(): {
            "email": entry_2.get(),
            "password": entry_3.get(),
        }
    }
    if len(entry_1.get()) == 0 or len(entry_3.get()) == 0:
        messagebox.showinfo(title="website", message="entry field empty")
    else:
        # ok = messagebox.askokcancel(title="website", message=f"these are the details entered:\nEmail: {entry_1.get()}"
        #                                                      f"\nPassword: {entry_3.get()}\n is it ok to save ")
        # if ok:

        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
            entry_1.delete(0, END)
            entry_3.delete(0, END)


def search_pass():
    website=entry_1.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="error",message="no file exist")
    else:
        if website in data:
            email= data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title="website",message=f"Email :{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="no entry",message="no such entry")


screen = Tk()
screen.title("PASSWORD_MANAGER")
screen.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)

img = Image.open("mypass.jpeg")
img = img.resize((250, 250))  # PIL solution
img = ImageTk.PhotoImage(img)
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="website:")
website.grid(row=1, column=0)

entry_1 = Entry(width=35)
entry_1.focus()
entry_1.grid(row=1, column=1, columnspan=1)

email = Label(text="Email/username:")
email.grid(row=2, column=0)
entry_2 = Entry(width=35)
entry_2.insert(0, "ishangupta409@gmail.com")
entry_2.grid(row=2, column=1, columnspan=2)

password = Label(text="password:")
password.grid(row=3, column=0)

entry_3 = Entry(width=21)
entry_3.grid(row=3, column=1)

# buttons
search_button =Button(text="search",command=search_pass)
search_button.grid(row=1,column=2)
g_password = Button(text="generate_password", command=generate_password)
g_password.grid(row=3, column=2)
add_button = Button(text="ADD", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

screen.mainloop()
