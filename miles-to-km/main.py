from tkinter import *

window = Tk()
window.title("Miles to KM Convertor")
window.minsize(width=300, height=100)
window.config(pady=50, padx=20)

distance_km = 0

input_miles = Entry(width = 7)
input_miles.grid(row = 0, column = 1, padx = 10, pady = 10)
# input_miles.config(padx = 10, pady = 10)


miles_label = Label(text = "Miles")
miles_label.grid(row = 0, column = 2, padx = 10, pady = 10)

label_km = Label(text=f"is equal to {distance_km}")
label_km.grid(row = 1, column = 1)
# label_km.config(pady = 20)


def calculate_km():
    distance = float(input_miles.get())
    distance_km = distance * 1.6
    distance_km = round(distance_km, 2)
    label_km.config(text=f"Is equal to {distance_km} km.")


button = Button(text="Calculate", command=calculate_km)
button.grid(row = 2, column = 1)
# button.config(pady = 20)
window.mainloop()
