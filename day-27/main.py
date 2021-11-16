import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI")
window.minsize(width = 500, height = 500)
window.config(padx = 20, pady = 20)

my_label = Label(text = "New Text", font = ("Arial", 24, "bold"))
my_label.grid(row = 0, column = 0)

def clicked_button():
    my_label.config(text = "Button has been clicked")
    print("Button clicked")

button = Button(text = "Click Me", command = clicked_button)
button.grid(row = 2, column = 3)

button_2 = Button(text = "New Button")
button_2.grid(row = 3, column = 2)
input = Entry(width = 10)
input.grid(row = 8, column = 8)
print(input.get())

window.mainloop()
