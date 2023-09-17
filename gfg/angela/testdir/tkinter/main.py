from tkinter import *

def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title('My First GUI Program')

window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New Click me")
new_button.grid(row=0, column=2)

# Input
input = Entry(width=10)
input.grid(row=2, column=3)

window.mainloop() 