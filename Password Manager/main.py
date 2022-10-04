from tkinter import *
from tkinter import messagebox
import passwordgen
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    password_entry.delete(0, END)
    password = passwordgen.RandomPassword()
    password_entry.insert(0, password.get_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website_data = website_entry.get()
    username_data = email_entry.get()
    password_data = password_entry.get()

    new_entry = {
        website_data:
                    {
                        "email": username_data,
                        "password": password_data
                    }
    }

    if len(website_data) == 0:
        messagebox.showerror(title="Empty entries! ", message="The website data is empty ")

    elif len(username_data) == 0:
        messagebox.showerror(title="Empty entries! ", message="The email/username data is empty ")

    elif len(password_data) == 0:
        messagebox.showerror(title="Empty entries! ", message="The password data is empty ")

    else:

        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are the entries: \nEmail: {username_data} \nPassword:"
                                               f" {password_data}\n Click on 'ok' to add the entries in your file")

        if is_ok:
            with open("password_data.json", mode="r") as data:
                data_dict = json.load(data)
                data_dict.update(new_entry)

            with open("password_data.json", mode="w") as data:
                json.dump(data_dict, data, indent=4)
                # data_entry = f"{website_data} | {username_data} | {password_data}"
                # data.write(data_entry)
                # data.write("\n")
                messagebox.showinfo(title="Prompt", message="The entry has been added")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

    # website_entry.delete(0, END)
    # password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.config(font="Courier")
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.config(width=55)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.config(font="Courier")
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.config(width=55)
email_entry.insert(0, "shreyanshgarhewal@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.config(font="Courier")
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.config(width=35)
password_entry.grid(row=3, column=1)

generate_button = Button()
generate_button.config(text="Generate for me", font=("Courier", 8), command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button()
add_button.config(text="Add", width=30, font="Courier", command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
