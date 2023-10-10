from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
            }
        }

    if website == '' or password == '':
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message="These are the details entered: \n Email: {}\nPassword: {}\nIs it okay to save?"
                            .format(email, password))
        if is_ok:
            try: 
                with open("data.json", "r") as file:
                #Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as file:               
                    #Saving the updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
# -------------------------- Find Password ---------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="website", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data exists for {website}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)


#Creating canvas for image
canvas = Canvas(height=200, width=200)
myImage = PhotoImage(file='logo.png')
canvas.create_image(80, 100, image=myImage)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ayush618officer@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)


#Buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop() 