import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for letter in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_name.get()
    email = email_input.get()
    pwd = password_input.get()
    if len(website) == 0 or len(email) == 0 or len(pwd) == 0:
        messagebox.showinfo("Information", "You have left some fields empty, please check the form before submitting.")
    else:
        is_ok = messagebox.askokcancel(website,
                                       f"Please check the following info: \n Email: {email} \n Password: {pwd} \n Is it okay to save?")
        # messagebox.showinfo("Information", "This is a message box")
        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": pwd
                }
            }
            try:
                file = open("data.json", "r")
                data = json.load(file)
            except FileNotFoundError:
                file = open("data.json", "w")
                json.dump(new_data, file, indent=3)
            except json.decoder.JSONDecodeError:
                file = open("data.json", "w")
                json.dump(new_data, file, indent=3)
            else:
                data.update(new_data)
                file = open("data.json", "w")
                # data = json.load(file)
                json.dump(data, file, indent=3)
            finally:
                file.close()
                website_name.delete(0, END)
                password_input.delete(0, END)

            # with open("data.json","w") as file:
            #     json.dump(data)

            # with open("passwords.txt", "a") as f:
            #     f.write(f"{website_name.get()} | {email_input.get()} | {password_input.get()} \n")
            #     website_name.delete(0, END)
            #     password_input.delete(0, END)


def search_credentials():
    website = website_name.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title=website,
                                message=f"Email: {data[website]['email']} \n Password: {data[website]['password']} ")
    except:
        messagebox.showinfo(message = "No records were found!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(height=200, width=200, padx=20, pady=20)
canvas = Canvas(width=200, height=200)
pw_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=pw_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website")
website_label.grid(row=1, column=0, pady=5)

website_name = Entry(width=21)
website_name.grid(row=1, column=1, columnspan=1)
website_name.focus()

search_button = Button(text="Search", background="white", width=15, command=search_credentials)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0, pady=5)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, pady=5)
email_input.insert(0, "saminbatra1@gmail.com")

password_label = Label(text="Password")
password_label.grid(row=3, column=0, pady=5)

password_input = Entry(width=21, show="*")
password_input.grid(row=3, column=1, pady=5, columnspan=1)

generate_button = Button(text="Generate Password", background="white", command=generate_password)
generate_button.grid(row=3, column=2, pady=5, padx=0)

add_button = Button(text="Add", width=35, background='white', highlightthickness=0, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
