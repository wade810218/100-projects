import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def  generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    
    shuffle(password_list)
    
    password = "".join(password_letters)
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:        
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                  f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)          
                    
            except FileNotFoundError:
                with open("data.json", "w") as data_file: 
                    json.dump(new_data, data_file, indent=4)  
                    
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:  
                    json.dump(data, data_file, indent=4)
                    
            finally:    
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
                    
    except FileNotFoundError:
            messagebox.showinfo(title="error", message="No Data File Found")
                
    #using except KeyError is not a good way:
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password} ")
        else:
            messagebox.showinfo(title="error", message=f"No details for {website} exists")
        
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Label
website_label = tk.Label(text = "Website:")
email_label = tk.Label(text = "Email/Username:")
password_label = tk.Label(text = "Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

#Entry
website_entry = tk.Entry()
email_entry = tk.Entry()
password_entry = tk.Entry()

website_entry.grid(row=1, column=1, columnspan=2 ,sticky="ew")
email_entry.grid(row=2, column=1, columnspan=2 ,sticky="ew")
password_entry.grid(row=3, column=1 ,sticky="ew")

website_entry.focus()
email_entry.insert(0, "minischnauzer@gmail.com")

#Button
generate_button = tk.Button(text = "Generate Password",highlightthickness=0  ,command= generate_password)
add_button = tk.Button(text = "Add", highlightthickness=0, command=save)
search_button = tk.Button(text = "Search", highlightthickness=0, command=find_password)

generate_button.grid(row=3, column=2, sticky="ew")
add_button.grid(row=4, column=1, columnspan=2 ,sticky="ew")
search_button.grid(row=1, column=2, sticky="ew")

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)

logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row=0, column=1)

window.mainloop()
