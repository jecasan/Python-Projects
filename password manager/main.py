from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pyperclip
import json

FONT = ("arial", 11)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    gen_pass = create_password()
    password_entry.insert(0, gen_pass)
    pyperclip.copy(gen_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("password_manager.json", "r") as file:
                # Reading old Data
                data = json.load(file)         
        except FileNotFoundError:
            with open("password_manager.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("password_manager.json", "w") as file:
                # Saving update
                json.dump(data, file, indent=4)
        finally: 
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
# ------------------------- SEARCH PASSWORD ---------------------------- #
def search_password():
    website = website_entry.get().title()
    try:
        with open("password_manager.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\n"
                                f"Password: {data[website]["password"]}")
        else:
            messagebox.showerror(title="Oops", message="Please enter a valid website.") 
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

website_var = StringVar()
email_var = StringVar()
password_var = StringVar()

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/email: ")
email_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_entry = Entry(window, width=25, font=FONT, textvariable=website_var)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(window, width=40, font=FONT, textvariable=email_var)
email_entry.insert(0, "johnerickasantor@gmail.com") 
email_entry.grid(column=1, columnspan=2, row=2)

password_entry = Entry(window, width=25, font=FONT, textvariable=password_var)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, columnspan=2, row=4)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1)



window.mainloop()
