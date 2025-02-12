from tkinter import *
from tkinter import messagebox
from password_generator import create_password
import pyperclip

FONT = ("arial", 11)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    gen_pass = create_password()
    password_entry.insert(0, gen_pass)
    pyperclip.copy(gen_pass)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}"
                            f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("password_manager.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
                
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

website_var = StringVar()
username_var = StringVar()
password_var = StringVar()

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_entry = Entry(window, width=40, font=FONT, textvariable=website_var)
website_entry.focus()
website_entry.grid(column=1, columnspan=2, row=1)

username_entry = Entry(window, width=40, font=FONT, textvariable=username_var)
username_entry.insert(0, "johnerickasantor@gmail.com") 
username_entry.grid(column=1, columnspan=2, row=2)

password_entry = Entry(window, width=25, font=FONT, textvariable=password_var)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, columnspan=2, row=4)



window.mainloop()