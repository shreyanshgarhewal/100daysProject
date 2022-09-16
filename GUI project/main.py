"""A Graphical User Interface program which calculates miles to km """

from tkinter import *

# A window is created where everything will be displayed
window = Tk()
window.title("miles to km converter")
window.minsize(width=200, height=80)


# A calling function which will be executed when the user click on the calculate button inside the window
def clicked():

    miles_input = float(entry.get())
    miles_to_km = round(miles_input * 1.609, 4)
    label2["text"] = str(miles_to_km)


# An entry element where user can give input in miles
entry = Entry(width=10)
entry.grid(row=0, column=1)

label1 = Label()
label1.config(text="is equal to: ", font=("Arial", 12))
label1.grid(row=1, column=0)

label2 = Label()
label2.config(text="0", font=("Arial", 12, "bold"))
label2.grid(row=1, column=1)

label3 = Label()
label3.config(text="km", font=("Arial", 12))
label3.grid(row=1, column=2)

label4 = Label()
label4.config(text="miles", font=("Arial", 12))
label4.grid(row=0, column=2)

# A button which pressed once the user has input the value to be created
button = Button(text="Calculate", command=clicked)
button.grid(row=2, column=1)


window.mainloop()
